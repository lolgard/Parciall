from fastapi import APIRouter, Depends
from app.core.database import get_session
from app.modules.Producto.unit_of_work import ProductoUnitOfWork
from app.modules.Ingrediente.service import IngredienteService
from app.modules.Ingrediente.schema import IngredienteCreate, IngredienteRead
router = APIRouter(prefix="/Ingredientes", tags= ["Ingredientes"])


def get_service(session=Depends(get_session)):
    uow=ProductoUnitOfWork(session)
    return IngredienteService(uow)


#create
@router.post("/", response_model=IngredienteRead)
def create_Ingrediente(data:IngredienteCreate, service:IngredienteService = Depends(get_service)):
    return service.Ingrediente_service_create(data)

#getall
@router.get("/", response_model=list[IngredienteRead])
def get_all(service:IngredienteService = Depends (get_service)):
    return service.get_all()

#get_porId
@router.get("/{id}", response_model=IngredienteRead)
def get_by_id(id:int,service:IngredienteService =Depends(get_service)):
    return service.get_by_id(id)
#update
@router.put("/{id}", response_model=IngredienteRead)
def update_ingrediente(id:int, data:IngredienteCreate, service:IngredienteService = Depends(get_service)):
    return service.update(id, data)

#delete
@router.delete("/{id}")
def get_by_id(id:int,service:IngredienteService =Depends(get_service)):
    return service.delete(id)