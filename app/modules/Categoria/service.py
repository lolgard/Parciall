from datetime import datetime

from fastapi import HTTPException
from sqlmodel import select
from app.modules.Categoria.model import Categoria
from app.modules.Categoria.schema import CategoriaCreate, CategoriaUpdate
from app.modules.Categoria.unit_of_work import CategoriaUnitOfWork


class CategoriaService:

    def __init__(self, uow: CategoriaUnitOfWork):
        self.uow = uow
    
    def categoria_service_create(self, data: CategoriaCreate):
        with self.uow as uow:
            if not data.nombre.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.categorias.get_by_name(data.nombre)
            if existente:
                raise HTTPException(400, "La categoría ya existe")
            if data.parent_id:
                padre = uow.categorias.get_by_id(data.parent_id)
                if not padre:
                    raise HTTPException(404, "La categoría padre no existe")
                
            categoria = Categoria(
                nombre=data.nombre,
                descripcion=data.descripcion,
                imagen_url=data.imagen_url,
                padre_id=data.parent_id
            )
            return uow.categorias.add(categoria)
        
    def get_all(self, include_inactivos: bool = False) ->list[Categoria]:
        with self.uow as uow:
            return uow.categorias.get_all(include_inactivos=include_inactivos)

    def get_by_id(self, categoria_id: int):
        with self.uow as uow:
            categoria = uow.categorias.get_by_id(categoria_id)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            return categoria

    def update(self, categoria_id: int, data: CategoriaUpdate):
        with self.uow as uow:
            categoria = uow.categorias.get_by_id(categoria_id, include_inactivos=True)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            
            update_data = data.model_dump(exclude_unset=True) if hasattr(data, "model_dump") else data.dict(exclude_unset=True)

            if "parent_id" in update_data:
                nuevo_padre_id = update_data["parent_id"]
                if nuevo_padre_id == categoria_id:
                    raise HTTPException(400, "Una categoría no puede ser su propio padre")
                if nuevo_padre_id is not None:
                    padre = uow.categorias.get_by_id(nuevo_padre_id)
                    if not padre:
                        raise HTTPException(404, "La categoría padre no existe")
                categoria.padre_id = nuevo_padre_id

            if "nombre" in update_data:
                categoria.nombre = update_data["nombre"]
            if "descripcion" in update_data:
                categoria.descripcion = update_data["descripcion"]
            if "imagen_url" in update_data:
                categoria.imagen_url = update_data["imagen_url"]

            if "activo" in update_data:
                activo = update_data["activo"]
                if activo is True:
                    if categoria.padre_id is not None:
                        padre_actual = uow.categorias.get_by_id(categoria.padre_id, include_inactivos=True)
                        if padre_actual and padre_actual.deleted_at is not None:
                            raise HTTPException(400, "No puedes activar esta categoría porque su padre está inactivo. Activa el padre primero o asígnale un nuevo padre.")
                    categoria.deleted_at = None
                elif activo is False:
                    # Soft delete
                    categoria.deleted_at = datetime.utcnow()
                    estrategia = update_data.get("estrategia_baja", "promote") or "promote"
                    children = uow._session.exec(select(Categoria).where(Categoria.padre_id == categoria_id)).all()
                    if estrategia == "cascade":
                        def inactivate_tree(cat):
                            cat.deleted_at = datetime.utcnow()
                            kids = uow._session.exec(select(Categoria).where(Categoria.padre_id == cat.id)).all()
                            for k in kids:
                                inactivate_tree(k)
                        for child in children:
                            inactivate_tree(child)
                    elif estrategia == "promote":
                        for child in children:
                            child.padre_id = None
            
            categoria.updated_at = datetime.utcnow()
            uow.categorias.update(categoria)
            return categoria

    def delete(self, categoria_id: int):
        with self.uow as uow:
            obj = uow.categorias.get_by_id(categoria_id)
            if not obj:
                raise HTTPException(404, "Categoría no encontrada")
            uow.categorias.delete(obj)