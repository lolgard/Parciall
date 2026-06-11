from datetime import datetime, timedelta
import secrets
from fastapi import HTTPException
from app.core.security import verify_password, create_access_token, hash_password
from app.modules.usuario.model import Usuario
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.modules.usuario.service import RefreshTokenService, UsuarioService
from app.modules.usuarioRol.model import UsuarioRol
from app.modules.auth.schema import LoginRequest, RegisterRequest, UpdateProfileRequest
from app.modules.usuario.schema import UsuarioUpdate

class AuthService:
    def __init__(self, uow: UsuarioUnitOfWork):
        self.uow = uow
        self.refresh_service = RefreshTokenService(self.uow)
        self.usuario_service = UsuarioService(self.uow)

    def login(self, data: LoginRequest):
        with self.uow:
            usuario = self.uow.usuarios.get_by_email(data.email)
            if not usuario:
                raise HTTPException(status_code=401, detail="Credenciales incorrectas")
            
            if not verify_password(data.password, usuario.password_hash):
                raise HTTPException(status_code=401, detail="Credenciales incorrectas")
            
            roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []

            token = create_access_token(
                data={"sub": str(usuario.id)},
                expires_delta=timedelta(hours=24)
            )
            
            refresh_token_string = secrets.token_urlsafe(32)
            refresh_token_expire = datetime.utcnow() + timedelta(days=7)
            
            self.refresh_service.create_token(
                user_id=usuario.id,
                token_hash=refresh_token_string,
                expire_at=refresh_token_expire
            )

            u_dict = usuario.dict()
            u_dict["roles"] = roles

            return {
                "access_token": token,
                "refresh_token": refresh_token_string,
                "usuario": u_dict
            }

    def register(self, data: RegisterRequest):
        with self.uow:
            existente = self.uow.usuarios.get_by_email(data.email)
            if existente:
                raise HTTPException(400, "Ya existe un usuario con ese email")
            
            pwd_hash = hash_password(data.password)
            
            usuario = Usuario(
                email=data.email,
                name=data.name,
                lastname=data.lastname,
                phone_number=data.phone_number,
                password_hash=pwd_hash
            )
            self.uow.usuarios.add(usuario)
            
            rel = UsuarioRol(
                usuario_id=usuario.id,
                rol_codigo="CLIENT",
                create_at=datetime.utcnow(),
                expires_at=datetime.utcnow() + timedelta(days=365)
            )
            self.uow.usuario_rol.add(rel)
            
            self.uow.usuarios.update(usuario)
            
            roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
            u_dict = usuario.dict()
            u_dict["roles"] = roles
            return u_dict

    def refresh_token(self, refresh_token_string: str):
        with self.uow:
            try:
                old_token = self.refresh_service.refresh(refresh_token_string)
            except HTTPException as e:
                raise e
                
            usuario = self.uow.usuarios.get_by_id(old_token.user_id)
            if not usuario:
                raise HTTPException(status_code=401, detail="Usuario no encontrado")
                
            new_access_token = create_access_token(
                data={"sub": str(usuario.id)},
                expires_delta=timedelta(hours=24)
            )
            
            new_refresh_string = secrets.token_urlsafe(32)
            self.refresh_service.create_token(
                user_id=usuario.id,
                token_hash=new_refresh_string,
                expire_at=datetime.utcnow() + timedelta(days=7)
            )
            
            return {
                "access_token": new_access_token,
                "refresh_token": new_refresh_string
            }

    def get_me(self, user_id: int):
        with self.uow:
            usuario = self.uow.usuarios.get_by_id(user_id)
            if not usuario:
                raise HTTPException(status_code=404, detail="Usuario no encontrado")
                
            roles = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
            u_dict = usuario.dict()
            u_dict["roles"] = roles
            return u_dict

    def update_me(self, user_id: int, data: UpdateProfileRequest):
        update_data = UsuarioUpdate(
            name=data.name,
            lastname=data.lastname,
            email=data.email,
            phone_number=data.phone_number,
            password_hash=data.password
        )
        return self.usuario_service.update(user_id, update_data)
