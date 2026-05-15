from sqlmodel import Relationship, SQLModel
from app.modules.usuario.model import Usuario


class Rol(SQLModel, table=True):
    code : str
    name  : str
    descripcion : str
    
    usuarios: list["Usuario"] = Relationship(back_populates="roles",link_model="UsuarioRol")