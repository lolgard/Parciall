
from datetime import datetime

from sqlmodel import Session, select

from app.core.repository import BaseRepository
from app.modules.usuario.model import Usuario
from app.modules.usuarioRol.model import UsuarioRol


class UsuarioRepository(BaseRepository):
    def __init__(self, session:Session):
        self.session=session

    def create(self, data):

        usuario = Usuario(**data.dict())
        usuario = self.session.add(usuario)

        return usuario
    
    def get_by_name(self, name: str) -> Usuario:
        return self.session.exec(
            select(Usuario).where(Usuario.name == name)
        ).first()
    
    def get_by_email(self, email: str) -> Usuario | None:
        return self.session.exec(
            select(Usuario).where(Usuario.email == email)
        ).first()

    def get_by_username(self, username: str) -> Usuario | None:
        if username.isdigit():
            return self.get_by_id(int(username))
        return self.session.exec(
            select(Usuario).where(Usuario.email == username)
        ).first()
    
    def get_by_id(self, id:int) -> Usuario | None:
        usuario = self.session.get(Usuario, id)

        if not usuario or usuario.deleted_at is not None:
            return None
        return usuario
    
    def get_all(self) -> list[Usuario]:
        usuarios =self.session.exec(
            select(Usuario).where(Usuario.deleted_at == None)
        ).all()
        for usuario in usuarios:
            self.session.refresh(usuario)
        return usuarios
    
    def update(self,usuario:Usuario) ->Usuario:
        self.session.add(usuario)
        self.session.flush()
        self.session.refresh(usuario)
        return usuario
    
    def delete(self,usuario:Usuario)-> None:

        usuario.deleted_at = datetime.utcnow()
        self.session.add(usuario)
        self.session.flush()
            
       #---------------------------Repository UsuarioRol---------------------------
    from app.modules.usuarioRol.model import UsuarioRol
class UsuarioRolRepository(BaseRepository):
    def __init__(self, session:Session):
            self.session=session

    def add(self,rel:UsuarioRol):
            self.session.add(rel)
            return rel
        
    def get_by_usuario(self,usuario_id:int)-> list[UsuarioRol]:
            return self.session.exec(
                select(UsuarioRol).where(
                    UsuarioRol.usuario_id == usuario_id
                    )
                ).all()
        
    def get_by_rol(self, rol_id: int) -> list[UsuarioRol]:
            return self.session.exec(
                select(UsuarioRol).where(
                    UsuarioRol.rol_id == rol_id
                )
            ).all()

    def delete(self, rel: UsuarioRol) -> None:
            self.session.delete(rel)
            self.session.flush()

    #----------------------------repository de refresh token--------------------------------------
    from datetime import datetime

from sqlmodel import Session, select

from app.modules.refreshToken.model import RefreshToken


class RefreshTokenRepository:

    def __init__(self, session: Session):
        self.session = session

    def create(self, token: RefreshToken) -> RefreshToken:
        self.session.add(token)
        self.session.flush()
        self.session.refresh(token)
        return token
    
    def get_by_id(self, token_id: int) -> RefreshToken | None:
        return self.session.get(RefreshToken, token_id)

    def get_by_token_hash(self, token_hash: str) -> RefreshToken | None:
        return self.session.exec(
            select(RefreshToken).where(
                RefreshToken.token_hash == token_hash
            )
        ).first()
    
    def get_by_user(self, user_id: int) -> list[RefreshToken]:
        return self.session.exec(
            select(RefreshToken).where(
                RefreshToken.user_id == user_id
            )
        ).all()
    
    def revoke(self, token: RefreshToken) -> RefreshToken:
        token.revoked_at = datetime.utcnow()
        self.session.add(token)
        self.session.flush()
        self.session.refresh(token)
        return token
    
    def delete(self, token: RefreshToken) -> None:
        self.session.delete(token)
        self.session.flush()