from fastapi import APIRouter, Depends, Query
from app.core.database import get_session
from app.modules.Categoria import service
from app.modules.Producto.unit_of_work import ProductoUnitOfWork
from app.modules.Producto.service import ProductoService
from app.modules.Producto.schema import PaginatedResponse, ProductoCreate, ProductoRead, ProductoUpdate
from app.core.deps import require_role
router = APIRouter(prefix="/productos", tags= ["productos"])

def get_service(session=Depends(get_session)):
    uow = ProductoUnitOfWork(session)
    return ProductoService(uow)

#create
@router.post("/", response_model=ProductoRead, dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def create_Producto(data:ProductoCreate, service:ProductoService = Depends(get_service)):
    return service.producto_service_create(data)
    
#getall
@router.get("/", response_model=PaginatedResponse[ProductoRead])
def get_all(
    page:         int       = Query(default=1,    ge=1,    description="Número de página"),
    page_size:    int       = Query(default=12,   ge=1, le=100, description="Items por página"),
    search:       str | None = Query(default=None, description="Buscar por nombre"),
    categoria_id: int | None = Query(default=None, description="Filtrar por categoría"),
    disponible:   bool | None = Query(default=None, description="Filtrar por disponibilidad"),
    stock_status: str | None = Query(default=None, description="Filtrar por stock (agotado, bajo)"),
    include_inactivos: bool = Query(default=False, description="Incluir eliminados logicamente"),
    service: ProductoService = Depends(get_service),
):
    return service.get_all_paginated(
        page, page_size, search=search, categoria_id=categoria_id, 
        disponible=disponible, stock_status=stock_status, include_inactivos=include_inactivos
    )
#get_porId
@router.get("/{id}", response_model=ProductoRead)
def get_by_id(id:int,service:ProductoService =Depends(get_service)):
    return service.get_by_id(id)
#update
@router.put("/{id}", response_model=ProductoRead, dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def update_producto(id:int, data:ProductoUpdate, service:ProductoService = Depends(get_service)):
    return service.update(id, data)
#delete
@router.delete("/{id}", dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def delete_producto(id:int, service:ProductoService =Depends(get_service)):
    return service.delete(id)
