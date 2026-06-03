
from datetime import datetime

from sqlmodel import Relationship, SQLModel,Field
from typing import TYPE_CHECKING, Optional



if TYPE_CHECKING:
    from app.modules.detallePedido.model import DetallePedido
    from app.modules.estadoPedido.model import EstadoPedido
    from app.modules.formaPago.model import FormaPago
    from app.modules.usuario.model import Usuario
    from app.modules.historialEstadoPedido.model import HistorialEstadoPedido
    from app.modules.pago.model import Pago

class Pedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id")
    direccion_entrega_id: Optional[int] = Field(default=None, foreign_key="direccionentrega.id")

    estado_codigo: str = Field(default="PENDIENTE", foreign_key="estadopedido.codigo")
    forma_pago_codigo: str = Field(default="EFECTIVO", foreign_key="formapago.codigo")

    subtotal: float = Field(description="Subtotal al momento del pedido")
    descuento: float = Field(default=0.0)
    costo_envio: float = Field(default=0.0)
    total: float = Field(gt=0)

    notas: Optional[str] = None
    nombre_cliente: Optional[str] = None
    telefono: Optional[str] = None
    ip_cliente: Optional[str] = None
    extra_data: Optional[str] = None

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: Optional[datetime] = None

    detalles_pedido: list["DetallePedido"] = Relationship(back_populates="pedido")
    estado_pedido: "EstadoPedido" = Relationship(back_populates="pedidos")
    formas_pago: Optional["FormaPago"] = Relationship(back_populates="pedidos")
    usuario: Optional["Usuario"] = Relationship(back_populates="pedidos")
    historial_estados: list["HistorialEstadoPedido"] = Relationship(back_populates="pedido")
    pagos: list["Pago"] = Relationship(back_populates="pedido")