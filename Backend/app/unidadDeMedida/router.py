from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.unidadDeMedida.service import UnidadDeMedidaService
from app.unidadDeMedida.schema import (
    UnidadDeMedidaCreate,
    UnidadDeMedidaUpdate,
    UnidadDeMedidaRead,
)

router = APIRouter(prefix="/unidades", tags=["unidades"])


def get_service(session=Depends(get_session)):
    return UnidadDeMedidaService(session)


@router.post("/", response_model=UnidadDeMedidaRead)
def create_unidad(data: UnidadDeMedidaCreate, service: UnidadDeMedidaService = Depends(get_service)):
    return service.create(data)


@router.get("/", response_model=list[UnidadDeMedidaRead])
def get_all(service: UnidadDeMedidaService = Depends(get_service)):
    return service.get_all()


@router.get("/{id}", response_model=UnidadDeMedidaRead)
def get_by_id(id: int, service: UnidadDeMedidaService = Depends(get_service)):
    return service.get_by_id(id)


@router.put("/{id}", response_model=UnidadDeMedidaRead)
def update_unidad(id: int, data: UnidadDeMedidaUpdate, service: UnidadDeMedidaService = Depends(get_service)):
    return service.update(id, data)


@router.delete("/{id}")
def delete_unidad(id: int, service: UnidadDeMedidaService = Depends(get_service)):
    return service.delete(id)
