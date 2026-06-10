import json
from datetime import datetime, timedelta
from fastapi import HTTPException

from app.modules.pedido.model import Pedido
from app.modules.pedido.schema import PedidoCreate, PedidoUpdate
from app.modules.usuario.schema import UsuarioRead
from app.modules.pedido.unit_of_work import PedidoUnitOfWork
from app.modules.historialEstadoPedido.model import HistorialEstadoPedido
from app.modules.detallePedido.model import DetallePedido
from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.formaPago.model import FormaPago
from app.modules.Producto.model import Producto
from app.core.config import settings

ESTADOS_VALIDOS = ["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO", "ENTREGADO", "CANCELADO"]
TRANSICIONES = {
    "PENDIENTE": ["CONFIRMADO", "CANCELADO"],
    "CONFIRMADO": ["EN_PREP", "CANCELADO"],
    "EN_PREP": ["LISTO", "CANCELADO"],
    "LISTO": ["ENTREGADO", "CANCELADO"],
    "ENTREGADO": [],
    "CANCELADO": []
}


class PedidoService:
    def __init__(self, uow: PedidoUnitOfWork):
        self.uow = uow

    async def create(self, data: PedidoCreate, current_user_id: int):
        with self.uow as uow:
            # 1. Validar dirección de entrega
            direccion = uow.direccion_entregas.get_by_id(data.direccion_entrega_id)
            if not direccion:
                raise HTTPException(404, "Dirección de entrega no encontrada")
            if str(direccion.usuario_id) != str(current_user_id):
                raise HTTPException(400, f"La dirección de entrega no pertenece al usuario autenticado (Dir.User: {direccion.usuario_id}, Auth.User: {current_user_id})")

            # 2. Validar forma de pago
            forma_pago = uow.formas_pago.get_by_codigo(data.forma_pago_codigo)
            if not forma_pago:
                raise HTTPException(404, "Forma de pago no encontrada")
            if not forma_pago.habilitado:
                raise HTTPException(400, "La forma de pago seleccionada no está habilitada")

            # 3. Validar productos, calcular subtotal y actualizar stock
            subtotal = 0.0
            for item in data.items:
                producto = uow.productos.get_by_id(item.producto_id)
                if not producto:
                    raise HTTPException(404, f"Producto con ID {item.producto_id} no encontrado")
                if not producto.disponible:
                    raise HTTPException(400, f"El producto '{producto.name}' no está disponible")
                if producto.stock_cantidad < item.cantidad:
                    raise HTTPException(400, f"Stock insuficiente para '{producto.name}'. Disponible: {producto.stock_cantidad}")
                
                # Descontar stock
                producto.stock_cantidad -= item.cantidad
                uow.productos.update(producto)
                
                # Sumar al subtotal
                subtotal += item.subtotal_snapshot

            # 4. Crear el Pedido
            pedido = Pedido(
                usuario_id=current_user_id,
                direccion_entrega_id=data.direccion_entrega_id,
                estado_codigo="PENDIENTE",
                forma_pago_codigo=data.forma_pago_codigo,
                subtotal=subtotal,
                descuento=0.0,
                costo_envio=0.0,
                total=subtotal,
                notas=data.notas
            )
            uow.pedidos.add(pedido)  # flush -> genera pedido.id

            # 5. Crear los DetallePedido
            for item in data.items:
                detalle = DetallePedido(
                    pedido_id=pedido.id,
                    producto_id=item.producto_id,
                    nombre_snapshot=item.nombre_snapshot,
                    cantidad=item.cantidad,
                    precio_snapshot=item.precio_snapshot,
                    subtotal_snapshot=item.subtotal_snapshot,
                    personalizacion=item.personalizacion if item.personalizacion is not None else [],
                )
                uow.detalles.add(detalle)

            # 6. Registrar en historial a través del repositorio
            h = HistorialEstadoPedido(
                pedido_id=pedido.id,
                estado_desde=None,
                estado_codigo="PENDIENTE",
                observaciones="Creación del pedido"
            )
            uow.historial.add(h)

            result = pedido

        await self._emit_ws_events(result.id, result.estado_codigo, result)
        return result
    async def get_all(self, current_user: UsuarioRead):
        ahora = datetime.utcnow()
        from datetime import timedelta
        
        cancelados_para_ws = []
        with self.uow as uow:
            pedidos = uow.pedidos.get_all()
            if not pedidos:
                return []
            
            # Auto-cancelar pedidos con más de 23h
            for p in pedidos:
                if p.estado_codigo not in ("ENTREGADO", "CANCELADO") and p.created_at:
                    if (ahora - p.created_at) > timedelta(hours=23):
                        estado_anterior = p.estado_codigo
                        p.estado_codigo = "CANCELADO"
                        uow.pedidos.update(p)
                        
                        for detalle in p.detalles_pedido:
                            producto = uow.productos.get_by_id(detalle.producto_id)
                            if producto:
                                producto.stock_cantidad += detalle.cantidad
                                uow.productos.update(producto)
                                
                        obs = "Cancelado automáticamente (pasaron más de 23 horas)"
                        h = HistorialEstadoPedido(
                            pedido_id=p.id, 
                            estado_desde=estado_anterior,
                            estado_codigo="CANCELADO", 
                            observaciones=obs
                        )
                        uow.historial.add(h)
                        cancelados_para_ws.append(p)

            # Si el usuario solo es cliente (CLIENT), filtrar sus propios pedidos
            is_employee = any(r in ["ADMIN", "PEDIDOS", "STOCK"] for r in current_user.roles)
            if not is_employee:
                pedidos = [p for p in pedidos if p.usuario_id == current_user.id]
        
        for p_cancelado in cancelados_para_ws:
            await self._emit_ws_events(p_cancelado.id, "CANCELADO", p_cancelado)
            
        return pedidos

    def get_by_id(self, pedido_id: int, current_user: UsuarioRead):
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            
            is_employee = any(r in ["ADMIN", "PEDIDOS", "STOCK"] for r in current_user.roles)
            if not is_employee and pedido.usuario_id != current_user.id:
                raise HTTPException(403, "Acceso denegado a este pedido")
            return pedido

    async def update(self, pedido_id: int, data: PedidoUpdate, current_user: UsuarioRead):
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            for field, value in data.dict(exclude_unset=True).items():
                if field == "estado_codigo" and value != pedido.estado_codigo:
                    await self.avanzar_estado(pedido.id, value, current_user)
                else:
                    setattr(pedido, field, value)
            return uow.pedidos.update(pedido)

    async def avanzar_estado(self, pedido_id: int, nuevo_estado: str, current_user: UsuarioRead):
        if nuevo_estado not in ESTADOS_VALIDOS:
            raise HTTPException(400, f"Estado inválido: {nuevo_estado}")
            
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
                
            estado_actual = pedido.estado_codigo
            roles = current_user.roles
            
            # 1. Validar transición de estado (flujo válido)
            if nuevo_estado not in TRANSICIONES.get(estado_actual, []):
                raise HTTPException(400, f"Transición no permitida de {estado_actual} a {nuevo_estado}")
                
            # 2. Validar permisos por rol
            # ADMIN → puede hacer cualquier transición
            # PEDIDOS → avanza todos los estados y puede cancelar
            # CLIENT → solo puede cancelar su propio pedido en estado PENDIENTE
            autorizado = False
            
            if "ADMIN" in roles:
                autorizado = True
            elif "PEDIDOS" in roles:
                # PEDIDOS puede avanzar o cancelar cualquier pedido
                autorizado = True
            elif "CLIENT" in roles:
                # CLIENT solo puede cancelar su propio pedido cuando está PENDIENTE
                if nuevo_estado == "CANCELADO" and estado_actual == "PENDIENTE":
                    if pedido.usuario_id == current_user.id:
                        autorizado = True
                    
            if not autorizado:
                raise HTTPException(
                    403,
                    f"No tenés permisos para cambiar el estado de {estado_actual} a {nuevo_estado}. "
                    f"Tus roles son: {roles}"
                )
                
            pedido.estado_codigo = nuevo_estado
            uow.pedidos.update(pedido)
            
            # Si el pedido se cancela, reponemos el stock de los productos
            if nuevo_estado == "CANCELADO":
                for detalle in pedido.detalles_pedido:
                    producto = uow.productos.get_by_id(detalle.producto_id)
                    if producto:
                        producto.stock_cantidad += detalle.cantidad
                        uow.productos.update(producto)
            
            # Registrar cambio en historial a través del repositorio
            obs = f"Cambio de estado por {current_user.name} ({', '.join(current_user.roles)})"
            h = HistorialEstadoPedido(
                pedido_id=pedido.id, 
                estado_desde=estado_actual,
                estado_codigo=nuevo_estado, 
                observaciones=obs
            )
            uow.historial.add(h)
            
            result = pedido
            
        await self._emit_ws_events(result.id, result.estado_codigo, result)
        return result

    def delete(self, pedido_id: int):
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(404, "Pedido no encontrado")
            uow.pedidos.delete(pedido)

    async def _emit_ws_events(self, pedido_id: int, destino: str, pedido_obj) -> None:
        from app.core.websocket import manager
        from app.modules.pedido.schema import PedidoRead
        
        EVENTOS_WS = {
            "PENDIENTE":  "NUEVO_PEDIDO",
            "CONFIRMADO": "PEDIDO_CONFIRMADO",
            "EN_PREP": "PEDIDO_EN_PREPARACION",
            "LISTO":      "PEDIDO_LISTO",
            "CANCELADO":  "PEDIDO_CANCELADO",
            "ENTREGADO":  "PEDIDO_ENTREGADO",
        }
        
        ROLES_POR_TRANSICION = {
            "PENDIENTE":  ["pedidos", "admin"],
            "CONFIRMADO": ["pedidos", "cocina", "admin"],
            "EN_PREP": ["cocina", "pedidos", "admin"],
            "LISTO":      ["pedidos", "admin"],
            "ENTREGADO":  ["pedidos", "admin"],
            "CANCELADO":  ["pedidos", "cocina", "admin"],
        }
        
        event_type = EVENTOS_WS.get(destino)
        if not event_type:
            return

        data = PedidoRead.from_orm(pedido_obj).dict()
        data["created_at"] = data["created_at"].isoformat() if data.get("created_at") else None
        data["updated_at"] = data["updated_at"].isoformat() if data.get("updated_at") else None
        
        await manager.broadcast_to_order(pedido_id, event_type, data)

        roles_a_notificar = ROLES_POR_TRANSICION.get(destino, [])
        if roles_a_notificar:
            await manager.broadcast_to_roles(roles_a_notificar, event_type, data)
