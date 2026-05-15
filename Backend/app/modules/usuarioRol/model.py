from datetime import datetime

from sqlmodel import Relationship, SQLModel, Field
from typing import Optional


class UsuarioRol(SQLModel, Table=True):
    usuario_id : Optional[int] = Field(default=None, foreign_key="usuario.id", primary_key=True) 
    rol_codigo : Optional[str] = Field(default=None, foreign_key="rol.code", primary_key=True)
    asignado_por_id:Optional[int] = Field(default=None, foreign_key="usuario.id")
    expires_at: datetime

    
    create_at:datetime
    
    
