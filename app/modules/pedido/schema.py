from datetime import datetime
from typing import Optional, List

from sqlmodel import SQLModel


class PedidoBase(SQLModel):
    usuario_id: int
    direccion_entrega_id: Optional[int] = None
    subtotal: float
    descuento: Optional[float] = 0.0
    costo_envio: Optional[float] = 50.0
    total: float
    notas: Optional[str] = None


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
