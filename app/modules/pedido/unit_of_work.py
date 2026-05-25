from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.pedido.repository import PedidoRepository


class PedidoUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.pedidos = PedidoRepository(session)
