from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from typing import List, Optional


class CategoriaBase(SQLModel):
    nombre: str
    descripcion: str
    imagen_url: Optional[str] = None
    parent_id: Optional[int] = None

class CategoriaCreate(CategoriaBase):
    pass    
class CategoriaRead(CategoriaBase):
    id: int
    created_at: datetime
    updated_at: datetime
    deleted_at: Optional[datetime] =None

class CategoriaUpdate(CategoriaBase):
    
    nombre:Optional[str] = None
    descripcion:Optional[str] = None
    imagen_url: Optional[str] = None
    parent_id: Optional[int] = None

class CategoryResponse(CategoriaBase):
    id:       int
    children: List["CategoryResponse"] = []  

    model_config = {"from_attributes": True}

CategoryResponse.model_rebuild()