from fastapi import APIRouter, Depends, Request
from fastapi.responses import RedirectResponse
from typing import List
from app.modules.pago.schema import PagoCreate, PagoRead, PagoUpdate
from app.modules.pago.service import PagoService
from app.modules.pago.repository import PagoRepository
from app.modules.pedido.unit_of_work import PedidoUnitOfWork
from app.core.database import get_session
from sqlmodel import Session
from app.core.deps import get_current_active_user
from app.modules.usuario.schema import UsuarioRead

router = APIRouter(prefix="/pagos", tags=["pagos"])

def get_pago_service(session: Session = Depends(get_session)):
    repo = PagoRepository(session)
    uow = PedidoUnitOfWork(session)
    return PagoService(repo, uow)

@router.get("/pedido/{pedido_id}", response_model=List[PagoRead])
def get_pagos_by_pedido(pedido_id: int, service: PagoService = Depends(get_pago_service)):
    return service.get_by_pedido_id(pedido_id)

@router.post("/", response_model=PagoRead)
def create_pago(pago: PagoCreate, service: PagoService = Depends(get_pago_service)):
    return service.create(pago)

@router.post("/preferencia/{pedido_id}")
def crear_preferencia_mp(
    pedido_id: int, 
    service: PagoService = Depends(get_pago_service),
    current_user: UsuarioRead = Depends(get_current_active_user)
):
    return service.crear_preferencia(pedido_id, current_user.id)

@router.patch("/{pago_id}", response_model=PagoRead)
def update_pago(pago_id: int, pago: PagoUpdate, service: PagoService = Depends(get_pago_service)):
    return service.update(pago_id, pago)

@router.post("/webhook")
async def mercado_pago_webhook(
    request: Request,
    service: PagoService = Depends(get_pago_service)
):
    topic = request.query_params.get("topic")
    resource_id = request.query_params.get("id")

    if not topic or not resource_id:
        try:
            body = await request.json()
            topic = body.get("type") or (body.get("action", "").split(".")[0] if "action" in body else None)
            data = body.get("data", {})
            resource_id = data.get("id")
        except Exception:
            pass
            
    if not topic or not resource_id:
        return {"status": "ignored", "reason": "Missing topic or id"}

    return await service.procesar_webhook_mp(topic, str(resource_id))

@router.get("/redirect")
def mp_redirect(status: str, preference_id: str = None, payment_id: str = None, external_reference: str = None):
    """
    Endpoint intermedio HTTPS (Ngrok) para que Mercado Pago pueda hacer auto_return.
    Redirige automáticamente al frontend en localhost.
    """
    # Mercado Pago sobreescribe el parámetro 'status' con su propio estado (ej. 'approved', 'rejected', 'in_process')
    if status in ["success", "pending", "approved", "in_process"]:
        url = "http://localhost:5174/pedido-confirmado"
        if external_reference:
            url += f"?order_id={external_reference}"
        return RedirectResponse(url=url)
    else:
        return RedirectResponse(url="http://localhost:5174/carrito")
