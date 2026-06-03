from fastapi import APIRouter, Depends
from typing import List
from app.modules.pago.schema import PagoCreate, PagoRead, PagoUpdate
from app.modules.pago.service import PagoService
from app.modules.pago.repository import PagoRepository
from app.modules.pedido.unit_of_work import PedidoUnitOfWork
from app.core.database import get_session
from sqlmodel import Session

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

@router.patch("/{pago_id}", response_model=PagoRead)
def update_pago(pago_id: int, pago: PagoUpdate, service: PagoService = Depends(get_pago_service)):
    return service.update(pago_id, pago)
