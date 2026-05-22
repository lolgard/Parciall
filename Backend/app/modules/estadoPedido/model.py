from sqlmodel import Field, Relationship, SQLModel

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.modules.pedido.model import Pedido
    from app.modules.detallePedido.model import DetallePedido

class EstadoPedido(SQLModel, table=True):
    codigo: str = Field(primary_key=True)
    descripcion: str
    orden: int
    es_terminal: bool

    pedido: "Pedido" = Relationship(back_populates="estado_pedido")
    detallePedido: "DetallePedido" = Relationship(back_populates="estado_pedido")

