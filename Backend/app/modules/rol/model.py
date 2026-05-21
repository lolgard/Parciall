from typing import TYPE_CHECKING, Optional
from sqlmodel import Field, Relationship, SQLModel
from app.modules.usuarioRol.model import UsuarioRol


if TYPE_CHECKING:

    from app.modules.usuario.model import Usuario

class Rol(SQLModel, table=True):
    __tablename__ = "rol"

    id: int | None = Field(default=None, primary_key=True)
    code: str = Field(unique=True)
    name: str
    descripcion: str
    

    rol_rel :list["UsuarioRol"] =Relationship(back_populates="rol")
