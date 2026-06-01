from sqlmodel import Session, select

from app.modules.historialEstadoPedido.model import HistorialEstadoPedido


class HistorialEstadoPedidoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, historial: HistorialEstadoPedido) -> HistorialEstadoPedido:
        self.session.add(historial)
        self.session.flush()
        return historial

    def get_by_pedido(self, pedido_id: int) -> list[HistorialEstadoPedido]:
        return self.session.exec(
            select(HistorialEstadoPedido)
            .where(HistorialEstadoPedido.pedido_id == pedido_id)
            .order_by(HistorialEstadoPedido.created_at)
        ).all()

    def get_ultimo_estado(self, pedido_id: int) -> HistorialEstadoPedido | None:
        return self.session.exec(
            select(HistorialEstadoPedido)
            .where(HistorialEstadoPedido.pedido_id == pedido_id)
            .order_by(HistorialEstadoPedido.created_at.desc())
        ).first()
