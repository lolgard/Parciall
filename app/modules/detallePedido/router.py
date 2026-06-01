from fastapi import APIRouter, Depends

from app.core.database import get_session
from app.modules.detallePedido.service import DetallePedidoService
from app.modules.detallePedido.schema import (
    DetallePedidoCreate,
    DetallePedidoRead,
)
from app.core.deps import require_role

router = APIRouter(prefix="/detalles", tags=["detalles"])


from app.modules.detallePedido.unit_of_work import DetallePedidoUnitOfWork

def get_service(session=Depends(get_session)):
    uow = DetallePedidoUnitOfWork(session)
    return DetallePedidoService(uow)


# Solo ADMIN puede crear detalles manualmente (normalmente se crean al crear pedido)
@router.post("/", response_model=DetallePedidoRead, dependencies=[Depends(require_role(["ADMIN"]))])
def create_detalle(data: DetallePedidoCreate, service: DetallePedidoService = Depends(get_service)):
    return service.create(data)


# ADMIN y PEDIDOS pueden ver los detalles de cualquier pedido
@router.get("/pedido/{pedido_id}", response_model=list[DetallePedidoRead], dependencies=[Depends(require_role(["ADMIN", "PEDIDOS"]))])
def get_by_pedido(pedido_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.get_by_pedido(pedido_id)


@router.get("/{pedido_id}/{producto_id}", response_model=DetallePedidoRead, dependencies=[Depends(require_role(["ADMIN", "PEDIDOS"]))])
def get_detalle(pedido_id: int, producto_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.get_by_id(pedido_id, producto_id)


# Solo ADMIN puede eliminar detalles
@router.delete("/{pedido_id}/{producto_id}", dependencies=[Depends(require_role(["ADMIN"]))])
def delete_detalle(pedido_id: int, producto_id: int, service: DetallePedidoService = Depends(get_service)):
    return service.delete(pedido_id, producto_id)
