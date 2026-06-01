from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.direccionEntrega.repository import DireccionEntregaRepository
from app.modules.usuario.repository import UsuarioRepository

class DireccionEntregaUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.direccion_entregas = DireccionEntregaRepository(session)
        self.usuarios = UsuarioRepository(session)
