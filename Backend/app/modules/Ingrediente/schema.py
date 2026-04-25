from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
class IngredienteBase(SQLModel):
    name : str
    description:str
    esAlergeno:bool = False

class IngredienteCreate(IngredienteBase):

    pass
class IngredienteRead(IngredienteBase):
    id:int
    created_at: datetime 
    updated_at: datetime 

class IngredienteUpdate(IngredienteBase):
    id:int
    name : Optional[str] =None
    description:Optional[str]=None
    esAlergeno:Optional[bool] =None
