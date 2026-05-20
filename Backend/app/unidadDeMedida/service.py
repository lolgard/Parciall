import datetime

from fastapi import HTTPException
from app.unidadDeMedida.model import UnidadDeMedida
from app.unidadDeMedida.schema import UnidadDeMedidaCreate
from app.unidadDeMedida.unit_of_work import UnidadDeMedidaUnitOfWork


class UnidadDeMedidaService:

    def __init__(self, session):
        self._session = session

    def create(self, data: UnidadDeMedidaCreate):
        with UnidadDeMedidaUnitOfWork(self._session) as uow:
            if not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.unidades.get_by_name(data.name)
            if existente:
                raise HTTPException(400, "La unidad ya existe")

            unidad = UnidadDeMedida(**data.dict())
            return uow.unidades.add(unidad)

    def get_all(self) -> list[UnidadDeMedida]:
        with UnidadDeMedidaUnitOfWork(self._session) as uow:
            return uow.unidades.get_all()

    def get_by_id(self, unidad_id: int):
        with UnidadDeMedidaUnitOfWork(self._session) as uow:
            unidad = uow.unidades.get_by_id(unidad_id)
            if not unidad:
                raise HTTPException(404, "Unidad de medida no encontrada")
            return unidad

    def update(self, unidad_id: int, data):
        with UnidadDeMedidaUnitOfWork(self._session) as uow:
            unidad = uow.unidades.get_by_id(unidad_id)
            if not unidad:
                raise HTTPException(404, "Unidad no encontrada")

            if data.name is not None:
                unidad.name = data.name
            if data.symbol is not None:
                unidad.symbol = data.symbol
            if data.type is not None:
                unidad.type = data.type

            return unidad

    def delete(self, unidad_id: int):
        with UnidadDeMedidaUnitOfWork(self._session) as uow:
            obj = uow.unidades.get_by_id(unidad_id)
            if not obj:
                raise HTTPException(404, "Unidad no encontrada")
            uow.unidades.delete(obj)
