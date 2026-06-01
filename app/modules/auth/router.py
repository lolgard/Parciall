from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlmodel import select
from pydantic import BaseModel
from typing import Optional
from datetime import datetime, timedelta

from app.core.database import get_session
from app.core.security import verify_password, create_access_token, decode_access_token, hash_password
from app.modules.usuario.model import Usuario
from app.modules.usuario.schema import UsuarioDetallesRead
from app.modules.usuario.service import UsuarioService
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.modules.usuarioRol.model import UsuarioRol

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

class RegisterRequest(BaseModel):
    email: str
    password: str
    name: str
    lastname: str
    phone_number: Optional[int] = None


@router.post("/login")
def login(data: LoginRequest, response: Response, session = Depends(get_session)):
    usuario = session.exec(select(Usuario).where(Usuario.email == data.email)).first()
    if not usuario:
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    if not verify_password(data.password, usuario.password_hash):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")
    
    roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []

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


@router.post("/register")
def register(data: RegisterRequest, session = Depends(get_session)):
    uow = UsuarioUnitOfWork(session)
    with uow:
        # Verificar email único
        existente = uow.usuarios.get_by_email(data.email)
        if existente:
            raise HTTPException(400, "Ya existe un usuario con ese email")
        
        # Hashear la contraseña
        pwd_hash = hash_password(data.password)
        
        usuario = Usuario(
            email=data.email,
            name=data.name,
            lastname=data.lastname,
            phone_number=data.phone_number,
            password_hash=pwd_hash
        )
        uow.usuarios.add(usuario)
        
        # Asignar rol de Cliente (CLIENT) automáticamente
        rel = UsuarioRol(
            usuario_id=usuario.id,
            rol_codigo="CLIENT",
            create_at=datetime.utcnow(),
            expires_at=datetime.utcnow() + timedelta(days=365)
        )
        uow.usuario_rol.add(rel)
        
        uow.usuarios.update(usuario)
        
        roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
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
