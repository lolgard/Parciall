from datetime import datetime
from typing import Optional
from sqlmodel import SQLModel

class PagoBase(SQLModel):
    pedido_id: int
    mp_payment_id: Optional[int] = None
    mp_status: Optional[str] = None
    mp_status_detail: Optional[str] = None
    transaction_amount: float = 0.0
    payment_method_id: Optional[str] = None
    external_reference: str
    idempotency_key: str

class PagoCreate(PagoBase):
    pass

class PagoRead(PagoBase):
    id: int
    created_at: datetime
    updated_at: datetime

class PagoUpdate(SQLModel):
    mp_payment_id: Optional[int] = None
    mp_status: Optional[str] = None
    mp_status_detail: Optional[str] = None
    transaction_amount: Optional[float] = None
    payment_method_id: Optional[str] = None
    external_reference: Optional[str] = None
    idempotency_key: Optional[str] = None
