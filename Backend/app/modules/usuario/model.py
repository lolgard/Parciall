from datetime import datetime
from typing import Optional


from sqlmodel import Field, Relationship, SQLModel

from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.rol.model import Rol
from app.modules.refreshToken.model import RefreshToken

class Usuario(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)    
    name: str
    lastname: str
    email:str
    phone_number:Optional[int] = Field(default=None)
    password_hash: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None

    
    refreshToken: list["RefreshToken"] = Relationship(back_populates="usuario")
    roles: list["Rol"] = Relationship(back_populates="usuarios", link_model="UsuarioRol")
    direccionEntrega: list["DireccionEntrega"] = Relationship(back_populates="usuario")