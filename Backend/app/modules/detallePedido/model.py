from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel


if TYPE_CHECKING:
    from app.modules.Producto.model import Producto
    from app.modules.pedido.model import Pedido



class DetallePedido(SQLModel, table=True):
    pedido_id: Optional[int] = Field(default=None, foreign_key="pedido.id",primary_key=True, ondelete="CASCADE")
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True, ondelete="CASCADE")
    cantidad: int = Field(not None, gt=1, description="La cantidad debe ser mayor a 1")

    #---------------------------snapshot(inmutables desde creacion):---------------------------
    nombre_snapshot: str = Field(not None, description="Nombre del producto al momento de realizar el pedido")
    precio_snapshot: float = Field(not None, gt=0, description="Precio del producto al momento de realizar el pedido")
    subtotal_snapshot: float = Field(not None, description="Subtotal del producto (precio_snapshot * cantidad) al momento de realizar el pedido")
    
    personalizacion: int

    #---------------------------audit fields:----------------------------
    created_at: datetime = Field(default_factory=datetime.utcnow)

    
    pedido: Optional["Pedido"] = Relationship(back_populates="detalles_pedido")
    producto: "Producto" = Relationship(back_populates="detalles_pedido")
    
  