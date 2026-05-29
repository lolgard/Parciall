from fastapi import APIRouter, Depends

from app.core.database import get_session
from app.modules.estadoPedido.service import EstadoPedidoService
from app.modules.estadoPedido.schema import EstadoPedidoCreate, EstadoPedidoRead

router = APIRouter(prefix="/estados", tags=["estados"])


from app.modules.estadoPedido.unit_of_work import EstadoPedidoUnitOfWork

def get_service(session=Depends(get_session)):
    uow = EstadoPedidoUnitOfWork(session)
    return EstadoPedidoService(uow)


@router.post("/", response_model=EstadoPedidoRead)
def create_estado(data: EstadoPedidoCreate, service: EstadoPedidoService = Depends(get_service)):
    return service.create(data)


@router.get("/", response_model=list[EstadoPedidoRead])
def get_all(service: EstadoPedidoService = Depends(get_service)):
    return service.get_all()


@router.get("/{codigo}", response_model=EstadoPedidoRead)
def get_by_codigo(codigo: str, service: EstadoPedidoService = Depends(get_service)):
    return service.get_by_codigo(codigo)


@router.put("/{codigo}", response_model=EstadoPedidoRead)
def update_estado(codigo: str, data: EstadoPedidoCreate, service: EstadoPedidoService = Depends(get_service)):
    return service.update(codigo, data)


@router.delete("/{codigo}")
def delete_estado(codigo: str, service: EstadoPedidoService = Depends(get_service)):
    return service.delete(codigo)
