from sqlmodel import SQLModel
from typing import Optional


class EstadoPedidoBase(SQLModel):
    codigo: str
    descripcion: str
    orden: int
    es_terminal: bool = False


class EstadoPedidoCreate(EstadoPedidoBase):
    pass


class EstadoPedidoRead(EstadoPedidoBase):
    pass


class EstadoPedidoUpdate(SQLModel):
    descripcion: Optional[str] = None
    orden: Optional[int] = None
    es_terminal: Optional[bool] = None
