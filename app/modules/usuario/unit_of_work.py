from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.usuario.repository import(
    UsuarioRepository,
    UsuarioRolRepository,
    RefreshTokenRepository
)


class UsuarioUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.usuarios = UsuarioRepository(session)
        self.usuario_rol = UsuarioRolRepository(session)
        self.refresh_tokens = RefreshTokenRepository(session)
