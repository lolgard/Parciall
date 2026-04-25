from http.client import HTTPException
from app.modules.Categoria.model import Categoria
from app.modules.Categoria.schema import CategoriaCreate


class CategoriaService:
    def __init__(self, uow):
        self.uow = uow
    
    def categoria_service_create(self, data: CategoriaCreate):
        with self.uow as uow:
            if not data.nombre.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")
            existente = uow.categorias.get_by_name(data.nombre)
            if existente:
                raise HTTPException(400, "La categoría ya existe")
            categoria = Categoria(**data.dict())
            return uow.categorias.add(categoria)
        
    def get_all(self):
        with self.uow as uow:
            return uow.categorias.get_all()

    def get_by_id(self, categoria_id: int):
        with self.uow as uow:
            categoria = uow.categorias.get_by_id(categoria_id)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            return categoria

    def update(self, categoria_id: int, data: CategoriaCreate):
        with self.uow as uow:
            categoria = uow.categorias.get_by_id(categoria_id)
            if not categoria:
                raise HTTPException(404, "Categoría no encontrada")
            categoria.nombre = data.nombre
            categoria.descripcion = data.descripcion
            categoria.imagen_url = data.imagen_url
            return categoria

    def delete(self, categoria_id: int):
        with self.uow as uow:
            obj = uow.categorias.get_by_id(categoria_id)
            if not obj:
                raise HTTPException(404, "Categoría no encontrada")
            uow.categorias.delete(obj)