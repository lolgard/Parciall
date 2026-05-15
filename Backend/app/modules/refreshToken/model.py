from datetime import datetime
from typing import Optional

from sqlmodel import Field, Relationship, SQLModel
from app.modules.usuario.model import Usuario

class RefreshToken (SQLModel,table = True):
    id:int
    usuario_id: Optional[int] = Field(default=None, foreign_key="usuario.id", ondelete="CASCADE")
    token_hash: str = Field(unique=True, index=True)
    
    expire_at : datetime
    revoked_at : Optional[datetime] = None
    created_at : datetime = Field(default_factory=datetime.utcnow)

    usuario: "Usuario" = Relationship(back_populates="refreshToken")