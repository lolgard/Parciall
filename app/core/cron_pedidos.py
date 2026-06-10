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
                stmt = select(Pedido).where(
                    Pedido.created_at <= cutoff_time,
                    Pedido.estado_codigo.notin_(["ENTREGADO", "CANCELADO"])
                )
                
                old_orders = db.exec(stmt).all()
                
                if old_orders:
                    # Encontrar el estado_id de "CANCELADO"
                    estado_stmt = select(EstadoPedido).where(EstadoPedido.codigo == "CANCELADO")
                    estado_cancelado = db.exec(estado_stmt).first()
                    
                    if not estado_cancelado:
                        print("Error: El estado CANCELADO no existe en la base de datos.")
                        continue
                        
                    canceled_count = 0
                    for order in old_orders:
                        # Crear el historial de estado
                        historial = HistorialEstadoPedido(
                            pedido_id=order.id,
                            estado_pedido_id=estado_cancelado.id,
                            fecha_inicio=datetime.utcnow()
                        )
                        db.add(historial)
                        
                        # Actualizar el pedido
                        order.estado_codigo = "CANCELADO"
                        db.add(order)
                        canceled_count += 1
                        
                    db.commit()
                    print(f"[CRON] Se auto-cancelaron {canceled_count} pedidos abandonados (+23h).")
                    
                    # Notificar a todos los clientes conectados al Dashboard/Pedidos
                    await manager.broadcast_pedidos()
                    
        except Exception as e:
            print(f"[CRON ERROR] Falló la auto-cancelación de pedidos: {e}")
            
        # Esperar 1 hora antes de volver a chequear (60 min * 60 sec)
        await asyncio.sleep(3600)
