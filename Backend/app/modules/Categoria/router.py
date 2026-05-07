from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.modules.Categoria.service import CategoriaService
from app.modules.Categoria.schema import CategoriaCreate
from app.modules.Categoria.schema import CategoriaRead
router = APIRouter(prefix="/categorias", tags= ["categorias"])


def get_service(session=Depends(get_session)):
    return CategoriaService(session)


#create
@router.post("/", response_model=CategoriaRead)
def create_Categoria(data:CategoriaCreate, service:CategoriaService = Depends(get_service)):
    return service.categoria_service_create(data)

#getall
@router.get("/", response_model=list[CategoriaRead])
def get_all(service:CategoriaService = Depends (get_service)):
    return service.get_all()
##agregar paginacion a get all


#get_porId
@router.get("/{id}", response_model=CategoriaRead)
def get_by_id(id:int,service:CategoriaService =Depends(get_service)):
    return service.get_by_id(id)

#update
@router.put("/{id}", response_model=CategoriaRead)
def update_categoria(id:int, data:CategoriaCreate, service:CategoriaService = Depends(get_service)):
    return service.update(id, data)

#delete
@router.delete("/{id}")
def get_by_id(id:int,service:CategoriaService =Depends(get_service)):
    return service.delete(id)