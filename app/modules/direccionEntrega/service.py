from fastapi import HTTPException

from app.modules.direccionEntrega.unit_of_work import DireccionEntregaUnitOfWork
from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.direccionEntrega.schema import DireccionEntregaCreate, DireccionEntregaUpdate
from app.modules.usuario.model import Usuario


class DireccionEntregaService:
    def __init__(self, uow: DireccionEntregaUnitOfWork):
        self.uow = uow

    def direccion_service_create(self, data: DireccionEntregaCreate):
        with self.uow as uow:
            # validar usuario si viene
            if data.usuario_id:
                usuario = uow._session.get(Usuario, data.usuario_id)
                if not usuario:
                    raise HTTPException(404, "Usuario no encontrado")

            direccion = DireccionEntrega(**data.dict())
            return uow.direccion_entregas.add(direccion)

    def get_all(self):
        with self.uow as uow:
            Direcciones = uow.direccion_entregas.get_all()
            if not Direcciones:
                raise HTTPException(404, "No se encontraron direcciones")
            return Direcciones

    def get_by_id(self, direccion_id: int):
        with self.uow as uow:
            direccion = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion:
                raise HTTPException(404, "Dirección no encontrada")
            return direccion

    def update(self, direccion_id: int, data: DireccionEntregaUpdate):
        with self.uow as uow:
            direccion = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion:
                raise HTTPException(404, "Dirección no encontrada")

            # aplicar campos opcionales
            for field, value in data.dict(exclude_unset=True).items():
                setattr(direccion, field, value)

            uow.direccion_entregas.update(direccion)
            uow._session.refresh(direccion)
            return direccion

    def delete(self, direccion_id: int):
        with self.uow as uow:
            direccion = uow.direccion_entregas.get_by_id(direccion_id)
            if not direccion:
                raise HTTPException(404, "Dirección no encontrada")
            uow.direccion_entregas.delete(direccion)
