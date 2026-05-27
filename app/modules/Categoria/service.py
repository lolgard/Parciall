from datetime import datetime

from fastapi import HTTPException
from app.modules.Categoria.model import Categoria
from app.modules.Categoria.schema import CategoriaCreate, CategoriaUpdate
from app.modules.Categoria.unit_of_work import CategoriaUnitOfWork


class CategoriaService:

    def __init__(self, session):
     self._session = session
    
    def categoria_service_create(self, data: CategoriaCreate):
        with CategoriaUnitOfWork(self._session) as uow:
            if not data.nombre.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.categorias.get_by_name(data.nombre)
            if existente:
                raise HTTPException(400, "La categoría ya existe")
            if data.parent_id:
                padre = uow.categorias.get_by_id(data.parent_id)
                if not padre:
                    raise HTTPException(404, "La categoría padre no existe")
                
            categoria = Categoria(**data.dict())
            return uow.categorias.add(categoria)
        
    def get_all(self) ->list[Categoria]:
        with CategoriaUnitOfWork(self._session) as uow:
            return uow.categorias.get_all()

    def get_by_id(self, categoria_id: int):
        with CategoriaUnitOfWork(self._session) as uow:
            categoria = uow.categorias.get_by_id(categoria_id)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            return categoria

    def update(self, categoria_id: int, data: CategoriaUpdate):
        with CategoriaUnitOfWork(self._session) as uow:
            categoria = uow.categorias.get_by_id(categoria_id)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            
            # Validar que no sea su propio padre
            if data.parent_id == categoria_id:
                raise HTTPException(400, "Una categoría no puede ser su propio padre")

            # Validar que el nuevo padre exista
            if data.parent_id:
                padre = uow.categorias.get_by_id(data.parent_id)
                if not padre:
                    raise HTTPException(404, "La categoría padre no existe")
                
            categoria.nombre = data.nombre
            categoria.descripcion = data.descripcion
            categoria.imagen_url = data.imagen_url
            categoria.updated_at = datetime.utcnow()
            return categoria

    def delete(self, categoria_id: int):
        with CategoriaUnitOfWork(self._session) as uow:
            obj = uow.categorias.get_by_id(categoria_id)
            if not obj:
                raise HTTPException(404, "Categoría no encontrada")
            uow.categorias.delete(obj)