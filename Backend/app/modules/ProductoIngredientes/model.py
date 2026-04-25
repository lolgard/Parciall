from sqlmodel import SQLModel,Field, Relationship
from typing import Optional
from app.modules.Producto.model import Producto
from app.modules.Ingrediente.model import Ingrediente

class ProductoIngrediente(SQLModel,table=True):
  
    producto_id: int = Field(foreign_key="producto.id", primary_key=True)
    ingrediente_id: int = Field(foreign_key="ingrediente.id", primary_key=True)

    es_removible:bool = Field(default=True)

    producto: "Producto" = Relationship(back_populates="ingredientes")
    ingrediente: "Ingrediente" = Relationship(back_populates="items")