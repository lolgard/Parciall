from sqlmodel import SQLModel, Field
from typing import Generic, List, Optional, TypeVar
from datetime import datetime
from app.modules.Categoria.schema import CategoriaRead
from app.modules.Ingrediente.schema import IngredienteRead

class ProductoBase(SQLModel):
    name: str
    price: float
    stock_cantidad: int
    disponible: bool = Field(default=True)
    imagen_url: Optional[str] = None
    descripcion: Optional[str] = None

class ProductoCategoriaRead(SQLModel):
    categoria_id: int
    es_principal: bool
    delete_at: Optional[datetime] = None
    imagen_url: Optional[str] = None
    categoria: Optional[CategoriaRead] = None

class ProductoIngredienteRead(SQLModel):
    ingrediente_id: int
    ingrediente: Optional[IngredienteRead] = None

class ProductoRead(ProductoBase):
    id: Optional[int] = None
    categorias: list[ProductoCategoriaRead] = []
    ingredientes: list[ProductoIngredienteRead] = []
    
class ProductoCreate(ProductoBase):
    categorias: list[int]
    ingredientes: Optional[list[int]] = None
    unidad_medida_id: int
  

class ProductoUpdate(SQLModel):
    name: Optional[str] = None
    price: Optional[float] = None
    stock_cantidad: Optional[int] = None
    disponible: Optional[bool] = None
    categorias: Optional[list[int]] = None
    ingredientes: Optional[list[int]] = None
    unidad_medida_id: Optional[int] = None
    imagen_url: Optional[str] = None
    descripcion: Optional[str] = None

class ProductoCategoriaCreate(SQLModel):
    categoria_id: int
    producto_id: int
    es_principal: bool = False

class ProductoCategoriaUpdate(SQLModel):
    es_principal: Optional[bool] = None

T = TypeVar("T")

class PaginatedResponse(SQLModel, Generic[T]):
    items:      List[T]
    page:       int
    page_size:  int
    total_pages: int