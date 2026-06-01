from sqlmodel import Session, select

from app.modules.formaPago.model import FormaPago

class FormaPagoRepository:
    def __init__(self, session: Session):
        self.session = session

    def get_by_codigo(self, codigo: str) -> FormaPago | None:
        return self.session.get(FormaPago, codigo)

    def get_all(self) -> list[FormaPago]:
        return self.session.exec(select(FormaPago)).all()
