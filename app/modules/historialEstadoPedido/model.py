from datetime import datetime
from sqlmodel import Relationship, SQLModel, Field
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from app.modules.pedido.model import Pedido
    from app.modules.estadoPedido.model import EstadoPedido

class HistorialEstadoPedido(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedido.id")
    estado_codigo: str = Field(foreign_key="estadopedido.codigo")
    observaciones: Optional[str] = None
    created_at: datetime = Field(default_factory=datetime.utcnow)
    
    pedido: Optional["Pedido"] = Relationship(back_populates="historial_estados")
    estado: Optional["EstadoPedido"] = Relationship()
