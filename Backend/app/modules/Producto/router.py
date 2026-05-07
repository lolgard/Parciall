from fastapi import APIRouter, Depends
from app.core.database import get_session
from app.modules.Producto.unit_of_work import ProductoUnitOfWork
from app.modules.Producto.service import ProductoService
from app.modules.Producto.schema import ProductoCreate, ProductoRead
router = APIRouter(prefix="/productos", tags= ["productos"])

def get_service(session=Depends(get_session)):
    return ProductoService(session)

#create
@router.post("/", response_model=ProductoRead)
def create_Producto(data:ProductoCreate, service:ProductoService = Depends(get_service)):
    return service.producto_service_create(data)
    
#getall
@router.get("/", response_model=list[ProductoRead])
def get_all(service:ProductoService = Depends (get_service)):
    return service.get_all()

#get_porId
@router.get("/{id}", response_model=ProductoRead)
def get_by_id(id:int,service:ProductoService =Depends(get_service)):
    return service.get_by_id(id)
#update
@router.put("/{id}", response_model=ProductoRead)
def update_producto(id:int, data:ProductoCreate, service:ProductoService = Depends(get_service)):
    return service.update(id, data)
#delete
@router.delete("/{id}")
def get_by_id(id:int,service:ProductoService =Depends(get_service)):
    return service.delete(id)
