from datetime import datetime

from sqlmodel import Session, select

from app.modules.estadoPedido.model import EstadoPedido


class EstadoPedidoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, estado: EstadoPedido) -> EstadoPedido:
        self.session.add(estado)
        self.session.flush()
        return estado

    def get_by_codigo(self, codigo: str) -> EstadoPedido | None:
        return self.session.get(EstadoPedido, codigo)

    def get_all(self) -> list[EstadoPedido]:
        return self.session.exec(select(EstadoPedido)).all()

    def update(self, estado: EstadoPedido) -> EstadoPedido:
        self.session.add(estado)
        self.session.flush()
        return estado

    def delete(self, estado: EstadoPedido) -> None:
        # logical delete not defined for this table; remove
        self.session.delete(estado)
