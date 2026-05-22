from typing import TYPE_CHECKING, Optional
from datetime import datetime
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.rol.model import Rol
    from app.modules.direccionEntrega.model import DireccionEntrega
    from app.modules.refreshToken.model import RefreshToken
    from app.modules.usuarioRol.model import UsuarioRol


 

class Usuario(SQLModel, table=True):
    __tablename__ = "usuario"
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

    usuarioRol: list["UsuarioRol"] = Relationship(back_populates="usuario")

    direccionEntrega: list["DireccionEntrega"] = Relationship(back_populates="usuario")