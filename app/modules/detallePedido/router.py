from fastapi import APIRouter, Depends

from app.core.database import get_session
from app.modules.detallePedido.service import DetallePedidoService
from app.modules.detallePedido.schema import (
    DetallePedidoCreate,
    DetallePedidoRead,
)

router = APIRouter(prefix="/detalles", tags=["detalles"])


from app.modules.detallePedido.unit_of_work import DetallePedidoUnitOfWork

def get_service(session=Depends(get_session)):
    uow = DetallePedidoUnitOfWork(session)
    return DetallePedidoService(uow)


@router.post("/", response_model=DetallePedidoRead)
def create_detalle(data: DetallePedidoCreate, service: DetallePedidoService = Depends(get_service)):
    return service.create(data)


@router.get("/pedido/{pedido_id}", response_model=list[DetallePedidoRead])
def get_by_pedido(pedido_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.get_by_pedido(pedido_id)


@router.get("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead)
def get_detalle(pedido_id: int, producto_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.get_by_id(pedido_id, producto_id)


@router.delete("/{pedido_id}/{producto_id}")
def delete_detalle(pedido_id: int, producto_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.delete(pedido_id, producto_id)
