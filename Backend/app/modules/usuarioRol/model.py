from datetime import datetime

from sqlmodel import Column, ForeignKey, Integer, Relationship, SQLModel, Field
from typing import Optional

from app.modules.rol.model import Rol
from app.modules.usuario.model import Usuario



class UsuarioRol(SQLModel, table=True):
    rol_codigo : Optional[str] = Field(default=None, foreign_key="rol.code", primary_key=True)
    expires_at: datetime

    
    usuario_id: int = Field(

        sa_column=Column(

            Integer,

            ForeignKey("usuario.id", ondelete="CASCADE"),

            primary_key=True,

            nullable=False,

        )

    )

    create_at:datetime
    

    usuario: Optional["Usuario"] = Relationship(back_populates="usuarioRol")
    rol: Optional["Rol"] = Relationship(back_populates="rol_rel")