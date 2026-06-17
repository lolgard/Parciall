from abc import ABC, abstractmethod
from typing import Optional, List
import uuid
import mercadopago
from app.core.config import settings
from app.modules.pago.model import Pago
from app.modules.pedido.model import Pedido
from app.modules.pedido.unit_of_work import PedidoUnitOfWork

class PaymentProvider(ABC):
    """
    Clase abstracta base para los proveedores de pago.
    Define el contrato para procesar un pago y devolver la URL de checkout (si aplica).
    """
    @abstractmethod
    def process_payment(self, pedido: Pedido, current_user_id: int, uow: PedidoUnitOfWork) -> Optional[str]:
        pass

class MercadoPagoProvider(PaymentProvider):
    """
    Proveedor específico para la pasarela Checkout Pro de Mercado Pago.
    """
    def process_payment(self, pedido: Pedido, current_user_id: int, uow: PedidoUnitOfWork) -> Optional[str]:
        # Obtener el email del usuario para la preferencia
        from app.modules.usuario.repository import UsuarioRepository
        usuario_repo = UsuarioRepository(uow._session)
        usuario = usuario_repo.get_by_id(current_user_id)
        email = usuario.email if usuario else "test_user_123@testuser.com"
        
        sdk = mercadopago.SDK(settings.MP_ACCESS_TOKEN)
        
        ngrok_url = settings.NGROK_URL.rstrip('/')
        
        preference_data = {
            "items": [
                {
                    "id": str(item.producto_id),
                    "title": item.nombre_snapshot,
                    "quantity": item.cantidad,
                    "unit_price": item.precio_snapshot
                } for item in pedido.detalles_pedido
            ],
            "payer": {
                "email": email
            },
            "back_urls": {
                "success": f"{ngrok_url}/pagos/redirect?status=success",
                "pending": f"{ngrok_url}/pagos/redirect?status=pending",
                "failure": f"{ngrok_url}/pagos/redirect?status=failure"
            },
            "auto_return": "approved",
            "notification_url": f"{ngrok_url}/pagos/webhook",
            "external_reference": str(pedido.id)
        }
        
        preference_response = sdk.preference().create(preference_data)
        checkout_url = None
        
        if preference_response.get("status") == 201:
            preference = preference_response["response"]
            checkout_url = preference.get("init_point") or preference.get("sandbox_init_point")
            
            pago = Pago(
                pedido_id=pedido.id,
                transaction_amount=pedido.total,
                mp_status="pending",
                payment_method_id="MERCADO_PAGO",
                external_reference=str(pedido.id),
                idempotency_key=str(uuid.uuid4())
            )
            uow.pagos.add(pago)
        else:
            import logging
            logger = logging.getLogger(__name__)
            logger.error(f"Error creando preferencia en Mercado Pago: {preference_response}")

        return checkout_url

class EfectivoProvider(PaymentProvider):
    """
    Proveedor por defecto para pagos en efectivo u offline.
    No requiere preferencia web externa ni link de cobro.
    """
    def process_payment(self, pedido: Pedido, current_user_id: int, uow: PedidoUnitOfWork) -> Optional[str]:
        # Para efectivo, simplemente creamos el registro de Pago indicando el método.
        # En muchos dominios, el pago en efectivo no se "crea" hasta que el cliente paga al repartidor, 
        # pero podemos registrar la intención.
        pago = Pago(
            pedido_id=pedido.id,
            transaction_amount=pedido.total,
            mp_status="pending", # O pending_cash
            payment_method_id="EFECTIVO",
            external_reference=f"efectivo_{pedido.id}",
            idempotency_key=str(uuid.uuid4())
        )
        uow.pagos.add(pago)
        
        return None

class DefaultProvider(PaymentProvider):
    """
    Proveedor para otros métodos genéricos que aún no tienen implementación avanzada.
    """
    def process_payment(self, pedido: Pedido, current_user_id: int, uow: PedidoUnitOfWork) -> Optional[str]:
        return None


class PaymentFactory:
    """
    Fábrica estática para devolver la implementación concreta del PaymentProvider.
    """
    @staticmethod
    def get_provider(forma_pago_codigo: str) -> PaymentProvider:
        codigo = forma_pago_codigo.upper()
        if codigo == "MERCADO_PAGO":
            return MercadoPagoProvider()
        elif codigo == "EFECTIVO":
            return EfectivoProvider()
        else:
            return DefaultProvider()
