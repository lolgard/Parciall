import asyncio
from datetime import datetime, timedelta
from sqlmodel import Session
from app.core.database import engine
from app.modules.pedido.model import Pedido
from app.modules.historialEstadoPedido.model import HistorialEstadoPedido
from app.modules.estadoPedido.model import EstadoPedido
from sqlalchemy import select
from app.core.websocket import manager

async def cancel_old_orders():
    """
    Tarea en segundo plano que corre cada 1 hora.
    Busca pedidos creados hace más de 23 horas que no estén en estado ENTREGADO ni CANCELADO.
    Los cambia a CANCELADO y notifica por WebSockets.
    """
    while True:
        try:
            with Session(engine) as db:
                cutoff_time = datetime.utcnow() - timedelta(hours=23)
                
                # Buscar pedidos viejos que no estén cancelados ni entregados
                stmt_activas = select(Pedido).where(
                    Pedido.created_at <= cutoff_time,
                    Pedido.estado_codigo.in_(["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"])
                )
                
                # Buscar PAGO_PENDIENTE abandonados hace más de 1 hora
                cutoff_mp = datetime.utcnow() - timedelta(hours=1)
                stmt_mp = select(Pedido).where(
                    Pedido.created_at <= cutoff_mp,
                    Pedido.estado_codigo == "PAGO_PENDIENTE"
                )
                
                old_orders = db.exec(stmt_activas).all()
                abandoned_mp = db.exec(stmt_mp).all()
                
                todas_expiradas = old_orders + abandoned_mp
                
                if todas_expiradas:
                    canceled_count = 0
                    for order in todas_expiradas:
                        estado_anterior = order.estado_codigo
                        
                        # Restaurar stock
                        for detalle in order.detalles_pedido:
                            from app.modules.Producto.model import Producto
                            producto = db.get(Producto, detalle.producto_id)
                            if producto:
                                producto.stock_cantidad += detalle.cantidad
                                db.add(producto)
                        
                        # Crear el historial de estado
                        obs = "Cancelado automáticamente (Carrito abandonado > 1h)" if estado_anterior == "PAGO_PENDIENTE" else "Cancelado automáticamente (+23h)"
                        historial = HistorialEstadoPedido(
                            pedido_id=order.id,
                            estado_desde=estado_anterior,
                            estado_codigo="CANCELADO",
                            observaciones=obs
                        )
                        db.add(historial)
                        
                        # Actualizar el pedido
                        order.estado_codigo = "CANCELADO"
                        db.add(order)
                        canceled_count += 1
                        
                    db.commit()
                    print(f"[CRON] Se auto-cancelaron {canceled_count} pedidos expirados.")
                    
                    # Notificar a todos los clientes conectados
                    await manager.broadcast_pedidos()
                    
        except Exception as e:
            print(f"[CRON ERROR] Falló la auto-cancelación de pedidos: {e}")
            
        # Esperar 1 minuto antes de volver a chequear
        await asyncio.sleep(60)
