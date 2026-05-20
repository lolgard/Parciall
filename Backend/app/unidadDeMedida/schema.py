from typing import Optional

from sqlmodel import SQLModel


class UnidadDeMedidaBase(SQLModel):
    name: str
    symbol: str
    type: str

class UnidadDeMedidaCreate(UnidadDeMedidaBase):
    pass

class UnidadDeMedidaRead(UnidadDeMedidaBase):
    id : int

class UnidadDeMedidaUpdate(SQLModel):
    name: Optional[str] = None
    symbol: Optional[str] = None
    type: Optional[str] = None

class UnidadDeMedidaDelete(SQLModel):
    id: int
