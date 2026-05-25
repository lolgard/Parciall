from datetime import datetime

from sqlmodel import Session, select

from app.modules.detallePedido.model import DetallePedido


class DetallePedidoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, detalle: DetallePedido) -> DetallePedido:
        self.session.add(detalle)
        self.session.flush()
        return detalle

    def get_by_id(self, pedido_id: int, producto_id: int) -> DetallePedido | None:
        detalle = self.session.get(DetallePedido, (pedido_id, producto_id))
        if not detalle or getattr(detalle, "deleted_at", None) is not None:
            return None
        return detalle

    def get_by_pedido(self, pedido_id: int) -> list[DetallePedido]:
        return self.session.exec(
            select(DetallePedido).where(
                (DetallePedido.pedido_id == pedido_id) & (DetallePedido.deleted_at == None)
            )
        ).all()

    def get_all(self) -> list[DetallePedido]:
        return self.session.exec(select(DetallePedido).where(DetallePedido.deleted_at == None)).all()

    def delete(self, detalle: DetallePedido) -> None:
        detalle.deleted_at = datetime.utcnow()
        self.session.add(detalle)
