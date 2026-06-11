from fastapi import APIRouter, Depends, HTTPException, Response, Request
from sqlmodel import Session

from app.core.database import get_session
from app.core.security import decode_access_token
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.modules.auth.schema import LoginRequest, RegisterRequest, UpdateProfileRequest
from app.modules.auth.service import AuthService

router = APIRouter(prefix="/auth", tags=["auth"])

def get_auth_service(session: Session = Depends(get_session)):
    uow = UsuarioUnitOfWork(session)
    return AuthService(uow)

@router.post("/login")
def login(data: LoginRequest, response: Response, service: AuthService = Depends(get_auth_service)):
    result = service.login(data)
    
    # Setear cookie HttpOnly para access_token (24hs)
    response.set_cookie(
        key="access_token",
        value=result["access_token"],
        httponly=True,
        samesite="lax",
        max_age=3600 * 24 # 24 horas
    )
    
    # Setear cookie HttpOnly para refresh_token (7 dias)
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        samesite="lax",
        max_age=3600 * 24 * 7 # 7 días
    )
    
    return result["usuario"]

@router.post("/refresh")
def refresh_token(request: Request, response: Response, service: AuthService = Depends(get_auth_service)):
    refresh_token_string = request.cookies.get("refresh_token")
    if not refresh_token_string:
        raise HTTPException(status_code=401, detail="Refresh token no proporcionado")
        
    try:
        result = service.refresh_token(refresh_token_string)
    except HTTPException as e:
        response.delete_cookie("access_token")
        response.delete_cookie("refresh_token")
        raise e
        
    response.set_cookie(
        key="access_token",
        value=result["access_token"],
        httponly=True,
        samesite="lax",
        max_age=3600 * 24
    )
    
    response.set_cookie(
        key="refresh_token",
        value=result["refresh_token"],
        httponly=True,
        samesite="lax",
        max_age=3600 * 24 * 7
    )
    
    return {"message": "Tokens actualizados"}

@router.post("/register")
def register(data: RegisterRequest, service: AuthService = Depends(get_auth_service)):
    return service.register(data)


@router.post("/logout")
def logout(response: Response):
    response.delete_cookie("access_token")
    response.delete_cookie("refresh_token")
    return {"message": "Sesión cerrada"}


def get_current_user_id(request: Request) -> int:
    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="No autenticado")
    
    payload = decode_access_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Token inválido o expirado")
    
    user_id_str = payload.get("sub")
    if not user_id_str:
        raise HTTPException(status_code=401, detail="Token sin ID")
        
    return int(user_id_str)


@router.get("/me")
def get_me(request: Request, service: AuthService = Depends(get_auth_service)):
    user_id = get_current_user_id(request)
    return service.get_me(user_id)


@router.patch("/me")
def update_me(data: UpdateProfileRequest, request: Request, service: AuthService = Depends(get_auth_service)):
    user_id = get_current_user_id(request)
    try:
        updated_user = service.update_me(user_id, data)
        return updated_user
    except Exception as e:
        if isinstance(e, HTTPException):
            raise e
        raise HTTPException(status_code=400, detail=str(e))
