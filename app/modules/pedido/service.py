from fastapi import HTTPException

from app.modules.pedido.model import Pedido
from app.modules.pedido.schema import PedidoCreate
from app.modules.pedido.unit_of_work import PedidoUnitOfWork


class PedidoService:
    def __init__(self, session):
        self._session = session

    def create(self, data: PedidoCreate):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = Pedido(**data.dict(exclude_unset=True))
            return uow.pedidos.add(pedido)

    def get_all(self):
        with PedidoUnitOfWork(self._session) as uow:
            pedidos = uow.pedidos.get_all()
            if not pedidos:
                raise HTTPException(404, "No se encontraron pedidos")
            return pedidos

    def get_by_id(self, pedido_id: int):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            return pedido

    def update(self, pedido_id: int, data: PedidoCreate):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            for field, value in data.dict(exclude_unset=True).items():
                setattr(pedido, field, value)
            return uow.pedidos.update(pedido)

    def delete(self, pedido_id: int):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            uow.pedidos.delete(pedido)
