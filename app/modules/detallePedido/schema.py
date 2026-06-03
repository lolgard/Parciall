from datetime import datetime
from typing import Optional

from sqlmodel import SQLModel


class DetallePedidoBase(SQLModel):
    pedido_id: int
    producto_id: int
    cantidad: int
    nombre_snapshot: str
    precio_snapshot: float
    subtotal_snapshot: float
    personalizacion: Optional[list[int]] = []


class DetallePedidoCreate(DetallePedidoBase):
    pass


class DetallePedidoRead(DetallePedidoBase):
    created_at: datetime


class DetallePedidoUpdate(SQLModel):
    cantidad: Optional[int] = None
    personalizacion: Optional[list[int]] = None
