from datetime import datetime

from fastapi import HTTPException
from sqlmodel import select

from app.modules.refreshToken.model import RefreshToken
from app.modules.usuario.repository import RefreshTokenRepository
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.modules.usuario.model import Usuario
from app.modules.usuario.schema import UsuarioCreate, UsuarioUpdate
from app.core.security import hash_password
from app.modules.usuarioRol.model import UsuarioRol
from datetime import timedelta


class UsuarioService:
    def __init__(self, session):
        self._session = session

    def usuario_service_create(self, data: UsuarioCreate):
        with UsuarioUnitOfWork(self._session) as uow:
            if not data.name or not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")

            # email único
            existente = self._session.exec(
                select(Usuario).where(Usuario.email == data.email)
            ).first()
            if existente:
                raise HTTPException(400, "Ya existe un usuario con ese email")

            # hashear contraseña
            if not data.password_hash:
                raise HTTPException(400, "La contraseña es obligatoria")

            data.password_hash = hash_password(data.password_hash)

            # crear y persistir directamente en la sesión para evitar inconsistencias
            usuario = Usuario(**data.dict(exclude={"roles"}))
            uow._session.add(usuario)
            uow._session.flush()

            roles_asignados = []
            if data.roles:
                for rol_code in set(data.roles):
                    rel = UsuarioRol(
                        usuario_id=usuario.id,
                        rol_codigo=rol_code,
                        create_at=datetime.utcnow(),
                        expires_at=datetime.utcnow() + timedelta(days=365)
                    )
                    uow._session.add(rel)
                    roles_asignados.append(rol_code)

            uow._session.commit()
            uow._session.refresh(usuario)

            u_dict = usuario.dict()
            u_dict["roles"] = roles_asignados
            return u_dict

    def get_all(self, exclude_role: str = None, role: str = None):
        with UsuarioUnitOfWork(self._session) as uow:
            usuarios = uow.usuarios.get_all()
            if not usuarios:
                return []
            
            result = []
            for u in usuarios:
                roles = [r.rol_codigo for r in u.usuarioRol] if u.usuarioRol else []
                
                if exclude_role and exclude_role in roles:
                    continue
                if role and role not in roles:
                    continue
                    
                u_dict = u.dict()
                u_dict["roles"] = roles
                result.append(u_dict)
            return result

    def get_by_id(self, usuario_id: int):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")
            
            u_dict = usuario.dict()
            u_dict["roles"] = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
            return u_dict

    def update(self, usuario_id: int, data: UsuarioUpdate):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            if data.name is not None:
                usuario.name = data.name
            if data.lastname is not None:
                usuario.lastname = data.lastname
            if data.email is not None:
                usuario.email = data.email
            if data.phone_number is not None:
                usuario.phone_number = data.phone_number
            if data.password_hash:
                usuario.password_hash = hash_password(data.password_hash)

            uow.usuarios.update(usuario)

            # Actualizar roles si fueron enviados
            if data.roles is not None:
                # Borrar roles viejos
                viejos_roles = uow._session.exec(select(UsuarioRol).where(UsuarioRol.usuario_id == usuario_id)).all()
                for rel in viejos_roles:
                    uow._session.delete(rel)
                
                # Asignar nuevos
                for rol_code in set(data.roles):
                    rel = UsuarioRol(
                        usuario_id=usuario.id,
                        rol_codigo=rol_code,
                        create_at=datetime.utcnow(),
                        expires_at=datetime.utcnow() + timedelta(days=365)
                    )
                    uow._session.add(rel)

            uow._session.commit()
            uow._session.refresh(usuario)
            
            u_dict = usuario.dict()
            u_dict["roles"] = [r.rol_codigo for r in usuario.usuarioRol] if usuario.usuarioRol else []
            return u_dict

    def delete(self, usuario_id: int):
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")
            uow.usuarios.delete(usuario)
            

            
class UsuarioRolService:
    def __init__(self, session):
        self._session = session

    def asignar_rol(self, usuario_id: int, rol_id: int) -> UsuarioRol:
        """Asigna un rol a un usuario. Lanza error si ya lo tiene."""
        with UsuarioUnitOfWork(self._session) as uow:
            # Verificar que el usuario existe
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            # Verificar que no tenga ya ese rol asignado
            relaciones = uow.usuario_roles.get_by_usuario(usuario_id)
            ya_tiene = any(r.rol_id == rol_id for r in relaciones)
            if ya_tiene:
                raise HTTPException(400, "El usuario ya tiene ese rol asignado")

            rel = UsuarioRol(
                usuario_id=usuario_id,
                rol_id=rol_id,
                expires_at=datetime.utcnow( )
            )
            return uow.usuario_roles.add(rel)

    def quitar_rol(self, usuario_id: int, rol_id: int) -> None:
        """Elimina la relación usuario-rol. Lanza error si no existe."""
        with UsuarioUnitOfWork(self._session) as uow:
            relaciones = uow.usuario_roles.get_by_usuario(usuario_id)
            rel = next((r for r in relaciones if r.rol_id == rol_id), None)

            if not rel:
                raise HTTPException(404, "El usuario no tiene ese rol asignado")

            uow.usuario_roles.delete(rel)

    def get_roles_de_usuario(self, usuario_id: int) -> list[UsuarioRol]:
        """Retorna todos los roles de un usuario."""
        with UsuarioUnitOfWork(self._session) as uow:
            usuario = uow.usuarios.get_by_id(usuario_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            roles = uow.usuario_roles.get_by_usuario(usuario_id)
            return roles  # lista vacía es válida, no es un 404

    def get_usuarios_de_rol(self, rol_id: int) -> list[UsuarioRol]:
        """Retorna todas las relaciones para un rol dado."""
        with UsuarioUnitOfWork(self._session) as uow:
            return uow.usuario_roles.get_by_rol(rol_id)
        
    #_----------------------------service de refresh token--------------------------------------
    
    
class RefreshTokenService:

    def __init__(self, session):
        self._session = session

    def create_token(
        self,
        user_id: int,
        token_hash: str,
        expire_at: datetime
    ):

        with UsuarioUnitOfWork(self._session) as uow:

            usuario = uow.usuarios.get_by_id(user_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            token = RefreshToken(
                user_id=user_id,
                token_hash=token_hash,
                expire_at=expire_at,
                created_at=datetime.utcnow(),
                revoked_at=None
            )

            uow.refresh_tokens.add(token)
            return token
    
    def validate_token(self, token_hash: str):

        with UsuarioUnitOfWork(self._session) as uow:

            token = uow.refresh_tokens.get_by_token_hash(token_hash)

            if not token:
                raise HTTPException(401, "Refresh token inválido")

            if token.revoked_at is not None:
                raise HTTPException(401, "Refresh token revocado")

            if token.expire_at < datetime.utcnow():
                raise HTTPException(401, "Refresh token expirado")

            return token
        
    def refresh(self, token_hash: str):

        with UsuarioUnitOfWork(self._session) as uow:

            token = uow.refresh_tokens.get_by_token_hash(token_hash)

            if not token:
                raise HTTPException(401, "Token inválido")

            if token.revoked_at is not None:
                raise HTTPException(401, "Token revocado")

            if token.expire_at < datetime.utcnow():
                raise HTTPException(401, "Token expirado")

            # revocar token viejo (rotación)
            token.revoked_at = datetime.utcnow()
            uow.refresh_tokens.update(token)

            return token
        
    def revoke_token(self, token_hash: str):

        with UsuarioUnitOfWork(self._session) as uow:

            token = uow.refresh_tokens.get_by_token_hash(token_hash)

            if not token:
                raise HTTPException(404, "Token no encontrado")

            if token.revoked_at is not None:
                raise HTTPException(400, "Token ya revocado")

            token.revoked_at = datetime.utcnow()
            uow.refresh_tokens.update(token)

            return {"message": "Token revocado"}
        
    def get_user_tokens(self, user_id: int):

        with UsuarioUnitOfWork(self._session) as uow:

            usuario = uow.usuarios.get_by_id(user_id)
            if not usuario:
                raise HTTPException(404, "Usuario no encontrado")

            return uow.refresh_tokens.get_by_user(user_id)