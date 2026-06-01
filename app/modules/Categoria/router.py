from fastapi import APIRouter, Depends
from app.core.database import get_session

from app.modules.Categoria.service import CategoriaService
from app.modules.Categoria.schema import CategoriaCreate, CategoriaUpdate
from app.modules.Categoria.schema import CategoriaRead
from app.core.deps import require_role

router = APIRouter(prefix="/categorias", tags= ["categorias"])


from app.modules.Categoria.unit_of_work import CategoriaUnitOfWork

def get_service(session=Depends(get_session)):
    uow = CategoriaUnitOfWork(session)
    return CategoriaService(uow)


#create
@router.post("/", response_model=CategoriaRead, dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def create_Categoria(data:CategoriaCreate, service:CategoriaService = Depends(get_service)):
    return service.categoria_service_create(data)

#getall
@router.get("/", response_model=list[CategoriaRead])
def get_all(service:CategoriaService = Depends (get_service)):
    return service.get_all()

#get_porId
@router.get("/{id}", response_model=CategoriaRead)
def get_by_id(id:int,service:CategoriaService =Depends(get_service)):
    return service.get_by_id(id)

#update
@router.put("/{id}", response_model=CategoriaRead, dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def update_categoria(id:int, data:CategoriaUpdate, service:CategoriaService = Depends(get_service)):
    return service.update(id, data)

#delete
@router.delete("/{id}", dependencies=[Depends(require_role(["ADMIN", "STOCK"]))])
def delete_categoria(id:int,service:CategoriaService =Depends(get_service)):
    return service.delete(id)