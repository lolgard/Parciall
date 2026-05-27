from sqlmodel import Column, ForeignKey, Integer, SQLModel, Field, Relationship
from typing import List, TYPE_CHECKING
from datetime import datetime
from app.modules.unidadDeMedida.model import UnidadDeMedida
from app.modules.detallePedido.model import DetallePedido

if TYPE_CHECKING:
    from app.modules.ProductoCategoria.model import ProductoCategoria
    from app.modules.ProductoIngredientes.model import ProductoIngrediente

    

class Producto(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str
    price: float
    stock_cantidad:int #=Field(0,stock_cantidad>=0)
    disponible: bool =Field(default =True)
    imagen_url: str | None = None
    
 

#guarda el tiempo en el que se modifica en la base 
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None

    # Relación: un producto puede estar en muchos items
    categorias: list["ProductoCategoria"] = Relationship(back_populates="producto")
    ingredientes: list["ProductoIngrediente"] = Relationship(back_populates="producto")

    # Relación: un producto tiene una unidad de medida
    unidad_medida_id: int = Field(
    foreign_key="unidad_medida.id"
)

    unidad_medida: "UnidadDeMedida" = Relationship(
    back_populates="productos",
    
)
    #relacion con detallePedido
    detalles_pedido: list["DetallePedido"] = Relationship(back_populates="producto")
    