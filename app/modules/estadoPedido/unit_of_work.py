from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.estadoPedido.repository import EstadoPedidoRepository


class EstadoPedidoUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.estados = EstadoPedidoRepository(session)
