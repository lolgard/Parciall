from sqlmodel import Field, SQLModel
from typing import Optional

class DireccionEntregaBase(SQLModel):
    alias : Optional[str] = None
    linea1 : int
    linea2 : Optional[int] = None
    ciudad : str
    provincia : str
    codigo_postal : str
    latitud : Optional[float] = None
    longitud : Optional[float] = None
    es_principal : bool = False

class DireccionEntregaCreate(DireccionEntregaBase):
    usuario_id: Optional[int] = None

class DireccionEntregaRead(DireccionEntregaBase):
    id: int
    usuario_id: Optional[int] = None

class DireccionEntregaUpdate(SQLModel):
    usuario_id: Optional[int] = None
    alias : Optional[str] = None
    linea1 : Optional[int] = None
    linea2 : Optional[int] = None
    ciudad : Optional[str] = None
    provincia : Optional[str] = None
    codigo_postal : Optional[str] = None
    latitud : Optional[float] = None
    longitud : Optional[float] = None
    es_principal : Optional[bool] = None


