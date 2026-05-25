from datetime import datetime

from sqlmodel import Session, select

from app.modules.pedido.model import Pedido


class PedidoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, pedido: Pedido) -> Pedido:
        self.session.add(pedido)
        self.session.flush()
        return pedido

    def get_by_id(self, id: int) -> Pedido | None:
        pedido = self.session.get(Pedido, id)
        if not pedido or getattr(pedido, "deleted_at", None) is not None:
            return None
        return pedido

    def get_all(self) -> list[Pedido]:
        return self.session.exec(select(Pedido).where(Pedido.deleted_at == None)).all()

    def update(self, pedido: Pedido) -> Pedido:
        self.session.add(pedido)
        self.session.flush()
        return pedido

    def delete(self, pedido: Pedido) -> None:
        pedido.deleted_at = datetime.utcnow()
        self.session.add(pedido)
