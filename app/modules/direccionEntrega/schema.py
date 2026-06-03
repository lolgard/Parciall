from sqlmodel import Field, SQLModel
from typing import Optional

class DireccionEntregaBase(SQLModel):
    alias : Optional[str] = None
    linea1 : str
    linea2 : Optional[str] = None
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
    linea1 : Optional[str] = None
    linea2 : Optional[str] = None
    ciudad : Optional[str] = None
    provincia : Optional[str] = None
    codigo_postal : Optional[str] = None
    latitud : Optional[float] = None
    longitud : Optional[float] = None
    es_principal : Optional[bool] = None


