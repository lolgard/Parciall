from typing import TYPE_CHECKING

from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.pedido.model import Pedido

class FormaPago(SQLModel, table=True):
    codigo : str = Field(primary_key=True)
    descripcion : str
    habilitado : bool = Field(default=True)

    
    pedidos: list["Pedido"] = Relationship(back_populates="formas_pago")
