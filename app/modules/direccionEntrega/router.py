from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.modules.direccionEntrega.service import DireccionEntregaService
from app.modules.direccionEntrega.schema import DireccionEntregaCreate, DireccionEntregaRead, DireccionEntregaUpdate
from app.modules.usuario.schema import UsuarioRead
from app.core.deps import get_current_active_user
from app.modules.direccionEntrega.unit_of_work import DireccionEntregaUnitOfWork

router = APIRouter(prefix="/direccionEntrega", tags=["direccionEntrega"])


def get_service(session=Depends(get_session)):
    uow = DireccionEntregaUnitOfWork(session)
    return DireccionEntregaService(uow)


@router.post("/", response_model=DireccionEntregaRead)
def create_direccion(
    data: DireccionEntregaCreate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: DireccionEntregaService = Depends(get_service)
):
    # Forzar usuario autenticado como creador de la dirección
    data.usuario_id = current_user.id
    return service.direccion_service_create(data)


@router.get("/", response_model=list[DireccionEntregaRead])
def get_all(
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: DireccionEntregaService = Depends(get_service)
):
    return service.get_all(current_user)


@router.get("/{id}", response_model=DireccionEntregaRead)
def get_by_id(
    id: int,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: DireccionEntregaService = Depends(get_service)
):
    return service.get_by_id(id, current_user)


@router.patch("/{id}", response_model=DireccionEntregaRead)
def update_direccion(
    id: int,
    data: DireccionEntregaUpdate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: DireccionEntregaService = Depends(get_service)
):
    return service.update(id, data, current_user)


@router.delete("/{id}")
def delete_direccion(
    id: int,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: DireccionEntregaService = Depends(get_service)
):
    return service.delete(id, current_user)
