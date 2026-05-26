from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel, Field


class PedidoBase(SQLModel):
    usuario_id: Optional[int] = None
    direccion_entrega_id: Optional[int] = None
    subtotal: float
    descuento: Optional[float] = 0.0
    costo_envio: Optional[float] = 0.0
    total: float
    notas: Optional[str] = None
    nombre_cliente: Optional[str] = None
    telefono: Optional[str] = None
    ip_cliente: Optional[str] = None
    extra_data: Optional[str] = None


class PedidoCreate(PedidoBase):
    estado_codigo: Optional[str] = None
    forma_pago_codigo: Optional[str] = None


class PedidoRead(PedidoBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None


class PedidoUpdate(SQLModel):
    subtotal: Optional[float] = None
    descuento: Optional[float] = None
    costo_envio: Optional[float] = None
    total: Optional[float] = None
    notas: Optional[str] = None
    estado_codigo: Optional[str] = None
    forma_pago_codigo: Optional[str] = None


# --- Guest checkout ---

class GuestOrderItemCreate(SQLModel):
    producto_id: int
    cantidad: int = Field(ge=1)
    nombre_snapshot: str
    precio_snapshot: float = Field(gt=0)
    subtotal_snapshot: float


class GuestOrderCreate(SQLModel):
    nombre_cliente: str
    telefono: str
    notas: Optional[str] = None
    items: List[GuestOrderItemCreate]


class GuestOrderResponse(SQLModel):
    id: int
    nombre_cliente: Optional[str]
    telefono: Optional[str]
    total: float
    subtotal: float
    created_at: datetime
