from sqlmodel import SQLModel,Field,Relationship
from typing import TYPE_CHECKING
from datetime import datetime
if TYPE_CHECKING:
    from app.modules.ProductoIngredientes.model import ProductoIngrediente

class Ingrediente(SQLModel,table=True):
    id: int | None = Field(default=None, primary_key=True)
    name : str
    description:str
    esAlergeno:bool = Field(default=True)


    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None
    
    items :list["ProductoIngrediente"] =Relationship(back_populates="ingrediente")