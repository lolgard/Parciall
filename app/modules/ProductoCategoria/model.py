from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, TYPE_CHECKING
from datetime import datetime

if TYPE_CHECKING:
    from app.modules.Categoria.model import Categoria
    from app.modules.Producto.model import Producto

class ProductoCategoria(SQLModel, table=True):
    producto_id: int = Field(foreign_key="producto.id", primary_key=True)
    categoria_id: int = Field(foreign_key="categoria.id", primary_key=True)
  
    es_principal:bool=Field(default=True)  
    created_at: datetime = Field(default_factory=datetime.utcnow)
   
    producto: "Producto" = Relationship(back_populates="categorias")
    categoria: "Categoria" = Relationship(back_populates="productos")
    
    
    
