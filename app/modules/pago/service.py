from fastapi import HTTPException
from app.modules.pago.model import Pago
from app.modules.pago.schema import PagoCreate, PagoUpdate
from app.modules.pago.repository import PagoRepository
from app.modules.pedido.unit_of_work import PedidoUnitOfWork
from app.modules.historialEstadoPedido.model import HistorialEstadoPedido
from app.modules.pago.provider import PaymentFactory
from app.core.config import settings
import mercadopago
import logging

logger = logging.getLogger(__name__)

class PagoService:
    def __init__(self, pago_repo: PagoRepository, uow: PedidoUnitOfWork):
        self.pago_repo = pago_repo
        self.uow = uow

    def get_by_pedido_id(self, pedido_id: int):
        return self.pago_repo.get_by_pedido_id(pedido_id)

    def create(self, data: PagoCreate):
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(data.pedido_id)
            if not pedido:
                raise HTTPException(status_code=404, detail="Pedido no encontrado")
            
            pago = Pago(**data.dict())
            return uow.pagos.add(pago)

    def update(self, pago_id: int, data: PagoUpdate):
        with self.uow as uow:
            pago = uow.pagos.get_by_id(pago_id)
            if not pago:
                raise HTTPException(status_code=404, detail="Pago no encontrado")
            
            for field, value in data.dict(exclude_unset=True).items():
                setattr(pago, field, value)
            
            return uow.pagos.update(pago)

    async def procesar_webhook_mp(self, topic: str, resource_id: str):
        if topic != "payment":
            return {"status": "ignored", "reason": f"Topic '{topic}' not handled"}

        # Instanciar el SDK
        sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)
        
        # Consultar el estado real del pago a la API de Mercado Pago
        payment_info = sdk.payment().get(resource_id)
        
        if payment_info.get("status") != 200:
            logger.error(f"Error al consultar el pago {resource_id} en MP: {payment_info}")
            return {"status": "error", "reason": "Could not fetch payment from MP"}
            
        mp_data = payment_info["response"]
        mp_status = mp_data.get("status")
        mp_status_detail = mp_data.get("status_detail")
        external_reference = mp_data.get("external_reference")
        
        # El external_reference contiene nuestro pedido_id (seteado al crear la preferencia)
        if not external_reference:
            return {"status": "ignored", "reason": "No external_reference found"}
            
        try:
            pedido_id = int(external_reference)
        except ValueError:
            return {"status": "error", "reason": "Invalid external_reference"}

        with self.uow as uow:
            # Buscar si el pago ya existe
            pagos = uow.pagos.get_by_pedido_id(pedido_id)
            if not pagos:
                # Si no existía, lo creamos
                pago = Pago(
                    pedido_id=pedido_id,
                    mp_payment_id=int(resource_id) if str(resource_id).isdigit() else None,
                    mp_status=mp_status,
                    mp_status_detail=mp_status_detail,
                    external_reference=external_reference,
                    idempotency_key=f"ipn_{resource_id}"
                )
                uow.pagos.add(pago)
            else:
                pago = pagos[0]
                pago.mp_payment_id = int(resource_id) if str(resource_id).isdigit() else None
                pago.mp_status = mp_status
                pago.mp_status_detail = mp_status_detail
                uow.pagos.update(pago)

            # Si el pago fue aprobado, avanzamos el Pedido a CONFIRMADO
            if mp_status == "approved":
                pedido = uow.pedidos.get_by_id(pedido_id)
                if pedido and pedido.estado_codigo in ["PENDIENTE", "PAGO_PENDIENTE"]:
                    estado_actual = pedido.estado_codigo
                    pedido.estado_codigo = "CONFIRMADO"
                    uow.pedidos.update(pedido)
                    
                    # Historial
                    obs = "Aprobado automáticamente por Webhook MP"
                    h = HistorialEstadoPedido(
                        pedido_id=pedido.id, 
                        estado_desde=estado_actual,
                        estado_codigo="CONFIRMADO", 
                        observaciones=obs
                    )
                    uow.historial.add(h)
                    
                    from app.modules.pedido.schema import PedidoRead
                    pedido_actualizado_dict = PedidoRead.from_orm(pedido).dict()
                    pedido_actualizado_dict["created_at"] = pedido_actualizado_dict["created_at"].isoformat() if pedido_actualizado_dict.get("created_at") else None
                    pedido_actualizado_dict["updated_at"] = pedido_actualizado_dict["updated_at"].isoformat() if pedido_actualizado_dict.get("updated_at") else None

        if mp_status == "approved" and 'pedido_actualizado_dict' in locals():
            from app.core.websocket import manager
            EVENTOS_WS = {"CONFIRMADO": "PEDIDO_CONFIRMADO"}
            ROLES_POR_TRANSICION = {"CONFIRMADO": ["pedidos", "cocina", "admin"]}
            
            await manager.broadcast_to_order(pedido_id, EVENTOS_WS["CONFIRMADO"], pedido_actualizado_dict)
            await manager.broadcast_to_roles(ROLES_POR_TRANSICION["CONFIRMADO"], EVENTOS_WS["CONFIRMADO"], pedido_actualizado_dict)
            
        return {"status": "ok"}

    def crear_preferencia(self, pedido_id: int, current_user_id: int) -> dict:
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(pedido_id)
            if not pedido:
                raise HTTPException(status_code=404, detail="Pedido no encontrado")
                
            provider = PaymentFactory.get_provider(pedido.forma_pago_codigo)
            checkout_url = provider.process_payment(
                pedido=pedido,
                current_user_id=current_user_id,
                uow=uow
            )
            
            return {"checkout_url": checkout_url}
