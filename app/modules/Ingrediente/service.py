from fastapi import HTTPException
from datetime import datetime
from app.modules.Ingrediente.model import Ingrediente
from app.modules.Ingrediente.schema import IngredienteCreate, IngredienteUpdate
from app.modules.Ingrediente.unit_of_work import IngredienteUnitOfWork


class IngredienteService:
    def __init__(self, uow: IngredienteUnitOfWork):
        self.uow = uow
    
    def Ingrediente_service_create(self, data: IngredienteCreate):
        with self.uow as uow:
            if not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.ingredientes.get_by_name(data.name)
            if existente:
                raise HTTPException(400, "El ingrediente ya existe")
            ingrediente = Ingrediente(**data.dict())
            return uow.ingredientes.add(ingrediente)
        
    def get_all(self, include_inactivos: bool = False):
        with self.uow as uow:
            ingrediente = uow.ingredientes.get_all(include_inactivos=include_inactivos)
            if not ingrediente:
                return []
            return ingrediente

    def get_by_id(self, ingrediente_id: int):
        with self.uow as uow:
            ingrediente = uow.ingredientes.get_by_id(ingrediente_id)
            if not ingrediente:
                raise HTTPException(404, "Ingrediente no encontrado")
            return ingrediente
    

    def update(self, ingrediente_id: int, data: IngredienteUpdate):
        with self.uow as uow:
            ingrediente = uow.ingredientes.get_by_id(ingrediente_id, include_inactivos=True)
            if not ingrediente:
                raise HTTPException(404, "Ingrediente no encontrado")
            
            if data.name is not None:
                ingrediente.name = data.name
            if data.description is not None:
                ingrediente.description = data.description
            if data.esAlergeno is not None:
                ingrediente.esAlergeno = data.esAlergeno
                
            if data.activo is True:
                ingrediente.deleted_at = None
            elif data.activo is False:
                ingrediente.deleted_at = datetime.utcnow()
                
            ingrediente.updated_at = datetime.utcnow()
            return ingrediente

    def delete(self, ingrediente_id: int):
        with self.uow as uow:
            obj = uow.ingredientes.get_by_id(ingrediente_id)
            if not obj:
                raise HTTPException(404, "Ingrediente no encontrado")
            uow.ingredientes.delete(obj)