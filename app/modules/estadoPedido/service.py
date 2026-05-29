from fastapi import HTTPException

from app.modules.estadoPedido.model import EstadoPedido
from app.modules.estadoPedido.schema import EstadoPedidoCreate
from app.modules.estadoPedido.unit_of_work import EstadoPedidoUnitOfWork


class EstadoPedidoService:
    def __init__(self, uow: EstadoPedidoUnitOfWork):
        self.uow = uow

    def create(self, data: EstadoPedidoCreate):
        with self.uow as uow:
            existente = uow.estados.get_by_codigo(data.codigo)
            if existente:
                raise HTTPException(400, "El estado ya existe")
            estado = EstadoPedido(**data.dict())
            return uow.estados.add(estado)

    def get_all(self):
        with self.uow as uow:
            return uow.estados.get_all()

    def get_by_codigo(self, codigo: str):
        with self.uow as uow:
            estado = uow.estados.get_by_codigo(codigo)
            if not estado:
                raise HTTPException(404, "Estado no encontrado")
            return estado

    def update(self, codigo: str, data: EstadoPedidoCreate):
        with self.uow as uow:
            estado = uow.estados.get_by_codigo(codigo)
            if not estado:
                raise HTTPException(404, "Estado no encontrado")
            estado.descripcion = data.descripcion
            estado.orden = data.orden
            estado.es_terminal = data.es_terminal
            return uow.estados.update(estado)

    def delete(self, codigo: str):
        with self.uow as uow:
            estado = uow.estados.get_by_codigo(codigo)
            if not estado:
                raise HTTPException(404, "Estado no encontrado")
            uow.estados.delete(estado)
