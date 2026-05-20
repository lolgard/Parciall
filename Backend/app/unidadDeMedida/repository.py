from datetime import datetime

from app.modules.Categoria.repository import CategoriaRepository
from app.core.repository import BaseRepository
from app.unidadDeMedida.model import UnidadDeMedida
from app.unidadDeMedida.schema import UnidadDeMedidaCreate
from sqlmodel import Session, select


class UnidadDeMedidaRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(self, data: UnidadDeMedidaCreate) -> UnidadDeMedida:
        unidad = UnidadDeMedida(**data.dict())
        self.session.add(unidad)
        return unidad

    def get_by_id(self, id: int) -> UnidadDeMedida | None:
        unidad = self.session.get(UnidadDeMedida, id)
        if not unidad or unidad.deleted_at is not None:
            return None
        return unidad

    def get_by_name(self, name: str) -> UnidadDeMedida | None:
        return self.session.exec(
            select(UnidadDeMedida).where(UnidadDeMedida.name == name)
        ).first()

    def update(self, unidad: UnidadDeMedida) -> UnidadDeMedida:
        self.session.add(unidad)
        self.session.flush()
        return unidad

    def add(self, unidad: UnidadDeMedida) -> UnidadDeMedida:
        self.session.add(unidad)
        self.session.flush()
        return unidad

    def get_all(self) -> list[UnidadDeMedida]:
        return self.session.exec(
            select(UnidadDeMedida).where(UnidadDeMedida.deleted_at == None)
        ).all()

    def delete(self, unidad: UnidadDeMedida) -> None:
        unidad.deleted_at = datetime.utcnow()
        self.session.add(unidad)
