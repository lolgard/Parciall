from sqlmodel import SQLModel, Field, Relationship
from typing import List, Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.modules.ProductoCategoria.model import ProductoCategoria

class Categoria(SQLModel, table=True):
    __tablename__ = "categoria"
    id: int | None = Field(default=None, primary_key=True)
    nombre:str
    descripcion:str
    imagen_url: str
    
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None

    padre_id: int | None = Field(default=None, foreign_key="categoria.id")


    productos: list["ProductoCategoria"] = Relationship(back_populates="categoria")

    parent: Optional["Categoria"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={
            "remote_side": "Categoria.id",
            "foreign_keys": "[Categoria.padre_id]",
        }
    )
    children: list["Categoria"] = Relationship(
        back_populates="parent",
        sa_relationship_kwargs={
            "foreign_keys": "[Categoria.padre_id]",
        }
    )