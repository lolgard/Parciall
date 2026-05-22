
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
    
    def get_by_name(self,name:str)-> Usuario:
        return self. session.exec(
            select(Usuario).where(Usuario.bane == name)
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
        return usuario
    
    def delete(self,usuario:Usuario)-> None:
        usuario.delete_at = datetime.utcnow(
            self.session.add(usuario)
        )
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

from app.modules.refreshToken import RefreshToken


class RefreshTokenRepository:

    def __init__(self, session: Session):
        self.session = session
