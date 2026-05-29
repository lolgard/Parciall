from fastapi import HTTPException

from app.modules.detallePedido.model import DetallePedido
from app.modules.detallePedido.schema import (
    DetallePedidoCreate,
)
from app.modules.detallePedido.unit_of_work import DetallePedidoUnitOfWork


class DetallePedidoService:
    def __init__(self, uow: DetallePedidoUnitOfWork):
        self.uow = uow

    def create(self, data: DetallePedidoCreate):
        with self.uow as uow:
            detalle = DetallePedido(**data.dict())
            return uow.detalles.add(detalle)

    def get_all(self):
        with self.uow as uow:
            detalles = uow.detalles.get_all()
            if not detalles:
                raise HTTPException(404, "No se encontraron detalles de pedido")
            return detalles

    def get_by_pedido(self, pedido_id: int):
        with self.uow as uow:
            return uow.detalles.get_by_pedido(pedido_id)

    def get_by_id(self, pedido_id: int, producto_id: int):
        with self.uow as uow:
            detalle = uow.detalles.get_by_id(pedido_id, producto_id)
            if not detalle:
                raise HTTPException(404, "Detalle no encontrado")
            return detalle

    def delete(self, pedido_id: int, producto_id: int):
        with self.uow as uow:
            detalle = uow.detalles.get_by_id(pedido_id, producto_id)
            if not detalle:
                raise HTTPException(404, "Detalle no encontrado")
            uow.detalles.delete(detalle)
