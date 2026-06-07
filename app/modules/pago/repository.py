from sqlmodel import Session, select
from typing import List, Optional

from app.modules.pago.model import Pago

class PagoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_id(self, pago_id: int) -> Optional[Pago]:
        statement = select(Pago).where(Pago.id == pago_id)
        return self.session.exec(statement).first()

    def get_by_pedido_id(self, pedido_id: int) -> List[Pago]:
        statement = select(Pago).where(Pago.pedido_id == pedido_id)
        return self.session.exec(statement).all()

    def get_by_mp_payment_id(self, mp_payment_id: int) -> Optional[Pago]:
        statement = select(Pago).where(Pago.mp_payment_id == mp_payment_id)
        return self.session.exec(statement).first()

    def add(self, pago: Pago) -> Pago:
        self.session.add(pago)
        self.session.flush()
        return pago

    def update(self, pago: Pago) -> Pago:
        self.session.add(pago)
        self.session.flush()
        return pago
