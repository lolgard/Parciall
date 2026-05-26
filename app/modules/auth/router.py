from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlmodel import select
from pydantic import BaseModel
from typing import Optional

from app.core.database import get_session
from app.core.security import verify_password, create_access_token, decode_access_token
from app.modules.usuario.model import Usuario
from app.modules.usuario.schema import UsuarioDetallesRead
from app.modules.usuario.service import UsuarioService

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(data: LoginRequest, response: Response, session = Depends(get_session)):
    usuario = session.exec(select(Usuario).where(Usuario.email == data.email)).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if not verify_password(data.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
    
    # Validar que no sea un cliente o que tenga permisos de backoffice
    if "ADMIN" not in roles and "STOCK" not in roles and "PEDIDOS" not in roles:
        raise HTTPException(status_code=403, detail="Acceso denegado: rol sin permisos de administrador")

    # Generar token
    token = create_access_token(data={"sub": str(usuario.id)})
    
    # Setear cookie HttpOnly
    response.set_cookie(
        key="access_token",
        value=token,
        httponly=True,
        samesite="lax",
        max_age=3600 * 24 * 7 # 7 días
    )
    
    # Devolver usuario con roles
    u_dict = usuario.dict()
    u_dict["roles"] = roles
    return u_dict

@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    return {"message": "Sesión cerrada"}

@router.get("/me")
def get_me(request: Request, session = Depends(get_session)):
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="No autenticado")
    
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    user_id_str = payload.get("sub")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="Token sin ID")
        
    usuario = session.exec(select(Usuario).where(Usuario.id == int(user_id_str))).first()
    if not usuario:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
        
    roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
    u_dict = usuario.dict()
    u_dict["roles"] = roles
    return u_dict
