from fastapi import APIRouter, Depends, Request

from app.core.database import get_session
from app.modules.pedido.service import PedidoService
from app.modules.pedido.schema import PedidoCreate, PedidoRead, PedidoConDetallesRead, PedidoUpdate
from app.core.deps import get_current_active_user, require_role
from app.modules.usuario.schema import UsuarioRead
from app.modules.pedido.unit_of_work import PedidoUnitOfWork

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


def get_service(session=Depends(get_session)):
    uow = PedidoUnitOfWork(session)
    return PedidoService(uow)


@router.post("/", response_model=PedidoRead)
def create_pedido(
    data: PedidoCreate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return service.create(data, current_user.id)


@router.get("/", response_model=list[PedidoConDetallesRead])
def get_all(
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return service.get_all(current_user)


@router.get("/{id}", response_model=PedidoConDetallesRead)
def get_by_id(
    id: int,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return service.get_by_id(id, current_user)


@router.put("/{id}", response_model=PedidoRead)
def update_pedido(
    id: int,
    data: PedidoUpdate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return service.update(id, data, current_user)


@router.delete("/{id}", dependencies=[Depends(require_role(["ADMIN"]))])
def delete_pedido(
    id: int,
    service: PedidoService = Depends(get_service)
):
    return service.delete(id)
