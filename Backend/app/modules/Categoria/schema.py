from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel
from typing import Optional


class CategoriaBase(SQLModel):
    nombre: str
    descripcion: str
    imagen_url: Optional[str] = None

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
