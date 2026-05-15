from datetime import datetime
from typing import Optional

from sqlmodel import Relationship, SQLModel, Field
from app.modules.usuario.model import Usuario

class DireccionEntrega(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    usuario_id: Optional[int] = Field(foreign_key="usuario.id", ondelete="CASCADE")
    alias : Optional[str] = Field(default=None)
    linea1 : int
    linea2 : Optional[int] = Field(default=None)
    ciudad : str
    provincia : str
    codigo_postal : str
    latitud : Optional[float] = Field(default=None)
    longitud : Optional[float] = Field(default=None)
    es_principal : bool = Field(default=False)

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = Field(default=None)


    usuario: "Usuario" = Relationship(back_populates="direccionEntrega")
