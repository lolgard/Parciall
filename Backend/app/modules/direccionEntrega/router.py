from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.modules.direccionEntrega.service import DireccionEntregaService
from app.modules.direccionEntrega.schema import DireccionEntregaCreate, DireccionEntregaRead, DireccionEntregaUpdate

router = APIRouter(prefix="/direccionEntrega", tags=["direccionEntrega"])


def get_service(session=Depends(get_session)):
    return DireccionEntregaService(session)


@router.post("/", response_model=DireccionEntregaRead)
def create_direccion(data: DireccionEntregaCreate, service: DireccionEntregaService = Depends(get_service)):
    return service.direccion_service_create(data)


@router.get("/", response_model=list[DireccionEntregaRead])
def get_all(service: DireccionEntregaService = Depends(get_service)):
    return service.get_all()


@router.get("/{id}", response_model=DireccionEntregaRead)
def get_by_id(id: int, service: DireccionEntregaService = Depends(get_service)):
    return service.get_by_id(id)


@router.put("/{id}", response_model=DireccionEntregaRead)
def update_direccion(id: int, data: DireccionEntregaUpdate, service: DireccionEntregaService = Depends(get_service)):
    return service.update(id, data)


@router.delete("/{id}")
def delete_direccion(id: int, service: DireccionEntregaService = Depends(get_service)):
    return service.delete(id)
