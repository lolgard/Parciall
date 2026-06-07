from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, BigInteger

if TYPE_CHECKING:
    from app.modules.pedido.model import Pedido


class Pago(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedido.id")
    mp_payment_id: Optional[int] = Field(default=None, sa_column=Column(BigInteger, unique=True))
    mp_status: Optional[str] = Field(default=None)
    mp_status_detail: Optional[str] = Field(default=None)
    transaction_amount: float = Field(default=0.0)
    payment_method_id: Optional[str] = Field(default=None)
    external_reference: str = Field(sa_column_kwargs={"unique": True})
    idempotency_key: str = Field(sa_column_kwargs={"unique": True})

    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)

    pedido: Optional["Pedido"] = Relationship(back_populates="pagos")
