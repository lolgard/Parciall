from sqlmodel import Field, Relationship, SQLModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.pedido.model import Pedido

class EstadoPedido(SQLModel, table=True):
    codigo: str = Field(primary_key=True)
    descripcion: str
    orden: int
    es_terminal: bool

    pedidos: list["Pedido"] = Relationship(back_populates="estado_pedido")

