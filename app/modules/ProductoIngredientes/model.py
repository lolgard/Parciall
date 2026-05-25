from sqlmodel import SQLModel,Field, Relationship
from typing import Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from app.modules.Producto.model import Producto
    from app.modules.Ingrediente.model import Ingrediente
    from app.modules.unidadDeMedida.model import UnidadDeMedida
class ProductoIngrediente(SQLModel,table=True):
  
    producto_id: int = Field(foreign_key="producto.id", primary_key=True)
    ingrediente_id: int = Field(foreign_key="ingrediente.id", primary_key=True)

    es_removible:bool = Field(default=True)

    producto: "Producto" = Relationship(back_populates="ingredientes")
    ingrediente: "Ingrediente" = Relationship(back_populates="items")
    
    unidad_medida_id: int = Field(
    foreign_key="unidad_medida.id"
)

    unidad_medida: "UnidadDeMedida" = Relationship(
    back_populates="producto_ingredientes"
)