from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime

class ProductoBase(SQLModel):
    name: str
    price: float
    stock_cantidad: int
    disponible: bool = Field(default=True)

class ProductoCategoriaRead(SQLModel):
    categoria_id: int
    es_principal: bool

class ProductoIngredienteRead(SQLModel):
    ingrediente_id: int

class ProductoRead(ProductoBase):
    id: Optional[int] = None
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] = None
    categorias: list[ProductoCategoriaRead] = []
    ingredientes: list[ProductoIngredienteRead] = []
    
class ProductoCreate(ProductoBase):
    categorias: list[int]
    ingredientes: Optional[list[int]] = None

class ProductoUpdate(ProductoBase):
    name: Optional[str] = None
    price: Optional[float] = None
    stock_cantidad: Optional[int] = None
    disponible: Optional[bool] = None
    categorias: Optional[list[int]] = None
    ingredientes: Optional[list[int]] = None

class ProductoCategoriaCreate(SQLModel):
    categoria_id: int
    producto_id: int
    es_principal: bool = False

class ProductoCategoriaUpdate(SQLModel):
    es_principal: Optional[bool] = None