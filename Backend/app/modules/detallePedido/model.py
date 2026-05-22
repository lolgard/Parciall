from typing import Optional

from sqlmodel import Field, SQLModel


class DetallePedidoBase(SQLModel):
    pedido_id: Optional[int] = Field(default=None, foreign_key="pedido.id",primary_key=True, ondelete="CASCADE")
    producto_id: Optional[int] = Field(default=None, foreign_key="producto.id", primary_key=True, ondelete="CASCADE")
    cantidad: int = Field(not None, check=lambda x: x >= 1, description="La cantidad debe ser mayor a 1")

    #---------------------------snapshot(inmutables desde creacion):---------------------------
    nombre_snapshot: str = Field(not None, description="Nombre del producto al momento de realizar el pedido")
    precio_snapshot: float = Field(not None, check=lambda x: x >= 0, description="Precio del producto al momento de realizar el pedido")
    subtotal_snap