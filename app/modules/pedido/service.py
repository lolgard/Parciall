import json

from fastapi import HTTPException

from app.modules.pedido.model import Pedido
from app.modules.pedido.schema import PedidoCreate, GuestOrderCreate, GuestOrderResponse, PedidoUpdate
from app.modules.pedido.unit_of_work import PedidoUnitOfWork
from app.modules.historialEstadoPedido.model import HistorialEstadoPedido

ESTADOS_VALIDOS = ["PENDIENTE", "CONFIRMADO", "EN_PREPARACION", "LISTO", "ENTREGADO", "CANCELADO"]
TRANSICIONES = {
    "PENDIENTE": ["CONFIRMADO", "CANCELADO"],
    "CONFIRMADO": ["EN_PREPARACION", "CANCELADO"],
    "EN_PREPARACION": ["LISTO"],
    "LISTO": ["ENTREGADO"],
    "ENTREGADO": [],
    "CANCELADO": []
}


class PedidoService:
    def __init__(self, session):
        self._session = session

    def create(self, data: PedidoCreate):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = Pedido(**data.dict(exclude_unset=True))
            if not pedido.estado_codigo:
                pedido.estado_codigo = "PENDIENTE"
            uow.pedidos.add(pedido)
            
            # Audit trail
            h = HistorialEstadoPedido(pedido_id=pedido.id, estado_codigo=pedido.estado_codigo, observaciones="Creación del pedido")
            self._session.add(h)
            return pedido

    def get_all(self):
        with PedidoUnitOfWork(self._session) as uow:
            pedidos = uow.pedidos.get_all()
            if not pedidos:
                return []
            return pedidos

    def get_by_id(self, pedido_id: int):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            return pedido

    def update(self, pedido_id: int, data: PedidoUpdate):
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            for field, value in data.dict(exclude_unset=True).items():
                if field == "estado_codigo" and value != pedido.estado_codigo:
                    self.avanzar_estado(pedido.id, value)
                else:
                    setattr(pedido, field, value)
            return uow.pedidos.update(pedido)

    def avanzar_estado(self, pedido_id: int, nuevo_estado: str):
        if nuevo_estado not in ESTADOS_VALIDOS:
            raise HTTPException(400, f"Estado inválido: {nuevo_estado}")
            
        with PedidoUnitOfWork(self._session) as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
                
            estado_actual = pedido.estado_codigo
            
            if nuevo_estado not in TRANSICIONES.get(estado_actual, []):
                raise HTTPException(400, f"Transición no permitida de {estado_actual} a {nuevo_estado}")
                
            pedido.estado_codigo = nuevo_estado
            uow.pedidos.update(pedido)
            
            # Audit trail
            h = HistorialEstadoPedido(pedido_id=pedido.id, estado_codigo=nuevo_estado, observaciones="Cambio de estado")
            self._session.add(h)
            
            return pedido

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
                estado_codigo="PENDIENTE"
            )
            uow.pedidos.add(pedido)  # flush → pedido.id asignado
            
            # Audit trail
            h = HistorialEstadoPedido(pedido_id=pedido.id, estado_codigo="PENDIENTE", observaciones="Guest Order checkout")
            self._session.add(h)

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
