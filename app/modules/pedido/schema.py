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


class PedidoItemCreate(SQLModel):
    producto_id: int
    cantidad: int = Field(ge=1)
    nombre_snapshot: str
    precio_snapshot: float = Field(gt=0)
    subtotal_snapshot: float
    personalizacion: Optional[List[int]] = []

class PedidoCreate(SQLModel):
    direccion_entrega_id: int
    forma_pago_codigo: str
    notas: Optional[str] = None
    items: List[PedidoItemCreate]


class PedidoRead(PedidoBase):
    id: int
    estado_codigo: Optional[str] = None
    forma_pago_codigo: Optional[str] = None
    checkout_url: Optional[str] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None

from app.modules.detallePedido.schema import DetallePedidoRead
from app.modules.usuario.schema import UsuarioRead

class HistorialEstadoPedidoRead(SQLModel):
    id: int
    estado_codigo: str
    observaciones: Optional[str] = None
    created_at: datetime

class PedidoConDetallesRead(PedidoRead):
    detalles_pedido: List[DetallePedidoRead] = []
    usuario: Optional[UsuarioRead] = None
    historial_estados: List[HistorialEstadoPedidoRead] = []


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
    personalizacion: Optional[List[int]] = []


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
