from fastapi import HTTPException
from app.modules.Ingrediente.model import Ingrediente
from app.modules.Ingrediente.schema import IngredienteCreate
from app.modules.Ingrediente.unit_of_work import IngredienteUnitOfWork


class IngredienteService:
    def __init__(self, session):
     self._session = session
    
    def Ingrediente_service_create(self, data: IngredienteCreate):
        with IngredienteUnitOfWork(self._session) as uow:
            if not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.ingredientes.get_by_name(data.name)
            if existente:
                raise HTTPException(400, "El ingrediente ya existe")
            ingrediente = Ingrediente(**data.dict())
            return uow.ingredientes.add(ingrediente)
        
    def get_all(self):
        with IngredienteUnitOfWork(self._session) as uow:
            ingrediente = uow.ingredientes.get_all()
            if not ingrediente:
                raise HTTPException(404, "No se encontraron ingredientes")
            return ingrediente

    def get_by_id(self, ingrediente_id: int):
        with IngredienteUnitOfWork(self._session) as uow:
            ingrediente = uow.ingredientes.get_by_id(ingrediente_id)
            if not ingrediente:
                raise HTTPException(404, "Ingrediente no encontrado")
            return ingrediente
    
    def update(self, ingrediente_id: int, data: IngredienteCreate):
        with IngredienteUnitOfWork(self._session) as uow:
            ingrediente = uow.ingredientes.get_by_id(ingrediente_id)
            if not ingrediente:
                raise HTTPException(404, "Ingrediente no encontrado")
            ingrediente.name = data.name
            ingrediente.description = data.description
            ingrediente.esAlergeno = data.esAlergeno
            return ingrediente

    def delete(self, ingrediente_id: int):
        with IngredienteUnitOfWork(self._session) as uow:
            obj = uow.ingredientes.get_by_id(ingrediente_id)
            if not obj:
                raise HTTPException(404, "Ingrediente no encontrado")
            uow.ingredientes.delete(obj)