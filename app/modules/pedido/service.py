import json

from fastapi import HTTPException

from app.modules.pedido.model import Pedido
from app.modules.pedido.schema import PedidoCreate, GuestOrderCreate, GuestOrderResponse
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

    def create_guest_order(
        self,
        data: GuestOrderCreate,
        client_ip: str,
        user_agent: str,
    ) -> GuestOrderResponse:
        from app.modules.detallePedido.model import DetallePedido

        subtotal = sum(item.subtotal_snapshot for item in data.items)
        extra = json.dumps({
            "user_agent": user_agent,
            "total_items": sum(item.cantidad for item in data.items),
        }, ensure_ascii=False)

        with PedidoUnitOfWork(self._session) as uow:
            pedido = Pedido(
                nombre_cliente=data.nombre_cliente,
                telefono=data.telefono,
                notas=data.notas,
                ip_cliente=client_ip,
                extra_data=extra,
                subtotal=subtotal,
                descuento=0.0,
                costo_envio=0.0,
                total=subtotal,
            )
            uow.pedidos.add(pedido)  # flush → pedido.id asignado

            for item in data.items:
                detalle = DetallePedido(
                    pedido_id=pedido.id,
                    producto_id=item.producto_id,
                    cantidad=item.cantidad,
                    nombre_snapshot=item.nombre_snapshot,
                    precio_snapshot=item.precio_snapshot,
                    subtotal_snapshot=item.subtotal_snapshot,
                    personalizacion=0,
                )
                self._session.add(detalle)

            return GuestOrderResponse.model_validate(pedido)
