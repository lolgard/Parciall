from fastapi import APIRouter, Depends, Query
from app.core.database import get_session

from app.modules.usuario.service import UsuarioService
from app.modules.usuario.schema import UsuarioCreate, UsuarioRead, UsuarioDetallesRead, UsuarioUpdate
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork

from app.core.deps import require_role

router = APIRouter(
    prefix="/usuarios",
    tags=["usuarios"],
    dependencies=[Depends(require_role(["ADMIN"]))]
)


def get_service(session=Depends(get_session)):
    uow = UsuarioUnitOfWork(session)
    return UsuarioService(uow)


@router.post("/", response_model=UsuarioRead)
def create_usuario(data: UsuarioCreate, service: UsuarioService = Depends(get_service)):
    return service.usuario_service_create(data)


@router.get("/", response_model=list[UsuarioRead])
def get_all(
    exclude_role: str = Query(None, description="Excluir usuarios con este rol"),
    role: str = Query(None, description="Filtrar por este rol"),
    service: UsuarioService = Depends(get_service)
):
    return service.get_all(exclude_role=exclude_role, role=role)


@router.get("/{id}", response_model=UsuarioDetallesRead)
def get_by_id(id: int, service: UsuarioService = Depends(get_service)):
    return service.get_by_id(id)


@router.patch("/{id}", response_model=UsuarioRead)
def update_usuario(id: int, data: UsuarioUpdate, service: UsuarioService = Depends(get_service)):
    return service.update(id, data)


@router.delete("/{id}")
def delete_usuario(id: int, service: UsuarioService = Depends(get_service)):
    return service.delete(id)
