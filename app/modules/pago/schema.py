from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel

class PagoBase(SQLModel):
    pedido_id: int
    mp_status: Optional[str] = None
    mp_status_detail: Optional[str] = None

class PagoCreate(PagoBase):
    pass

class PagoRead(PagoBase):
    id: int
    created_at: datetime
    updated_at: datetime

class PagoUpdate(SQLModel):
    mp_status: Optional[str] = None
    mp_status_detail: Optional[str] = None
