from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.modules.usuario.service import UsuarioService
from app.modules.usuario.schema import UsuarioCreate, UsuarioRead, UsuarioDetallesRead, UsuarioUpdate

router = APIRouter(prefix="/usuarios", tags=["usuarios"])


def get_service(session=Depends(get_session)):
    return UsuarioService(session)


@router.post("/", response_model=UsuarioRead)
def create_usuario(data: UsuarioCreate, service: UsuarioService = Depends(get_service)):
    return service.usuario_service_create(data)


@router.get("/", response_model=list[UsuarioRead])
def get_all(service: UsuarioService = Depends(get_service)):
    return service.get_all()


@router.get("/{id}", response_model=UsuarioDetallesRead)
def get_by_id(id: int, service: UsuarioService = Depends(get_service)):
    return service.get_by_id(id)


@router.put("/{id}", response_model=UsuarioRead)
def update_usuario(id: int, data: UsuarioUpdate, service: UsuarioService = Depends(get_service)):
    return service.update(id, data)


@router.delete("/{id}")
def delete_usuario(id: int, service: UsuarioService = Depends(get_service)):
    return service.delete(id)
