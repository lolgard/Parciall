
from datetime import datetime

from sqlmodel import Relationship, SQLModel,Field
from typing import TYPE_CHECKING, Optional

from app.modules.estadoPedido.model import EstadoPedido
from app.modules.formaPago.model import FormaPago 

if TYPE_CHECKING:
    from app.modules.detallePedido.model import DetallePedido


class Pedido(SQLModel, table=True):
    id : Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuario.id")
    direccion_entrega_id: int = Field(default=None, foreign_key="direccionentrega.id")
   # estado_codigo: str = Field(default="pendiente", foreign_key="estadoPedido.codigo"), agregar cuando se cree estado pedido
   # forma_pago_codigo: str = Field(not None, default="efectivo", foreign_key="formaPago.codigo"), agregar cuando se cree forma de pago
   
#---------------------------------snapshot  monetario-------------------------------
    subtotal: float = Field(description="Subtotal del pedido al momento de realizar el pedido")
    descuento: float =Field(default=0.0, description="Descuento aplicado al pedido al momento de realizar el pedido")
    costo_envio: float = Field(default=50.0, description="Costo de envio al momento de realizar el pedido")
    total: float=Field(not None, gt=0)

#--------------------------------atributos-------------------------------
    notas: str

#--------------------------------------------audit--------------------------------

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None

    detalles_pedido: list["DetallePedido"] = Relationship(back_populates="pedido")
    estado_pedido: Optional["EstadoPedido"] = Relationship(back_populates="pedidos")
    formas_pago: list["FormaPago"] = Relationship(back_populates="pedidos")
