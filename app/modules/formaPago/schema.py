from sqlmodel import SQLModel
from typing import Optional


class FormaPagoBase(SQLModel):
    codigo: str
    descripcion: str
    habilitado: bool = True


class FormaPagoCreate(FormaPagoBase):
    pass


class FormaPagoRead(FormaPagoBase):
    pass


class FormaPagoUpdate(SQLModel):
    descripcion: Optional[str] = None
    habilitado: Optional[bool] = None
