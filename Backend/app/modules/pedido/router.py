from fastapi import APIRouter, Depends

from app.core.database import get_session
from app.modules.pedido.service import PedidoService
from app.modules.pedido.schema import PedidoCreate, PedidoRead

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


def get_service(session=Depends(get_session)):
    return PedidoService(session)


@router.post("/", response_model=PedidoRead)
def create_pedido(data: PedidoCreate, service: PedidoService = Depends(get_service)):
    return service.create(data)


@router.get("/", response_model=list[PedidoRead])
def get_all(service: PedidoService = Depends(get_service)):
    return service.get_all()


@router.get("/{id}", response_model=PedidoRead)
def get_by_id(id: int, service: PedidoService = Depends(get_service)):
    return service.get_by_id(id)


@router.put("/{id}", response_model=PedidoRead)
def update_pedido(id: int, data: PedidoCreate, service: PedidoService = Depends(get_service)):
    return service.update(id, data)


@router.delete("/{id}")
def delete_pedido(id: int, service: PedidoService = Depends(get_service)):
    return service.delete(id)
