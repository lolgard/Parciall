from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.detallePedido.repository import DetallePedidoRepository


class DetallePedidoUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.detalles = DetallePedidoRepository(session)
