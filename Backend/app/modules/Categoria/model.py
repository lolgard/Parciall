from sqlmodel import SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.modules.ProductoCategoria.model import ProductoCategoria

class Categoria(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    nombre:str
    descripcion:str
    imagen_url: str
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None


    # Relación: una Categoria tiene muchos items
    
    productos: list["ProductoCategoria"] = Relationship(back_populates="categoria")