from datetime import datetime
from sqlmodel import Field, SQLModel
class UnidadDeMedida(SQLModel, table=True):
    id: int | None = Field (default = None, primary_key=True)
    name: str
    symbol: str
    type: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None
