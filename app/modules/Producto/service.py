

from math import ceil

from sqlmodel import Session

from app.modules.Producto.unit_of_work import ProductoUnitOfWork
from fastapi import HTTPException

from app.core.unit_of_work import BaseUnitOfWork
from app.core.logger import get_logger
from app.modules.Producto.model import Producto
from app.modules.Producto.schema import PaginatedResponse, ProductoCreate, ProductoRead, ProductoUpdate
from app.modules.ProductoCategoria.model import ProductoCategoria
from app.modules.ProductoIngredientes.model import ProductoIngrediente

logger = get_logger("service.producto")

class ProductoService():
    def __init__(self, session):
     self._session = session

    def producto_service_create(self, data: ProductoCreate):

        with ProductoUnitOfWork(self._session) as uow:

            if not data.name.strip():
                raise HTTPException(400, "El nombre no puede estar vacío")

            if data.price < 0:
                raise HTTPException(400, "El precio no puede ser negativo")

            if data.stock_cantidad < 0:
                raise HTTPException(400, "El stock no puede ser negativo")

            existente = uow.productos.get_by_name(data.name)

            if existente:
                raise HTTPException(400, "Ya existe un producto con ese nombre")

            # 1. validar que venga categoria
            if not data.categorias:
                raise HTTPException(
                    status_code=400,
                    detail="El producto debe tener una categoría"
                )

           
         #  crear producto 
            data_dict = data.dict(exclude={"categorias", "ingredientes"})
            producto = Producto(**data_dict)

            uow.productos.add(producto)

         #  categorías 
            for cat_id in set(data.categorias):

                categoria = uow.categorias.get_by_id(cat_id)
                if not categoria:
                   raise HTTPException(404, f"Categoria {cat_id} no existe")

                uow.producto_categorias.add(
                   ProductoCategoria(
                        producto_id=producto.id,
                        categoria_id=cat_id,
                        es_principal=False
                    )
               )

            #ingredientes 
            if data.ingredientes:
                for ingre_id in set(data.ingredientes):

                    ingrediente = uow.ingredientes.get_by_id(ingre_id)
                    if not ingrediente:
                       raise HTTPException(404, f"Ingrediente {ingre_id} no existe")

                    uow.producto_ingredientes.add(
                       ProductoIngrediente(
                           producto_id=producto.id,
                           ingrediente_id=ingre_id,
                           unidad_medida_id=producto.unidad_medida_id
                       )
                   )
            
            logger.info(f"Producto creado: id={producto.id} name='{producto.name}'")
            return producto

    def get_all_paginated(
        self,
        page: int,
        page_size: int,
        search: str | None = None,
        categoria_id: int | None = None,
    ) -> PaginatedResponse:
        if page < 1:
            raise HTTPException(400, "La página debe ser mayor a 0")
        if page_size < 1 or page_size > 100:
            raise HTTPException(400, "El tamaño de página debe estar entre 1 y 100")

        offset = (page - 1) * page_size

        with ProductoUnitOfWork(self._session) as uow:
            items, total = uow.productos.get_paginated(
                offset, page_size, search=search, categoria_id=categoria_id
            )
            # Serialize to ProductoRead while the ORM session is still active.
            # SQLModel table-model .dict() returns None for relationship fields,
            # so we must call model_validate() here before the session commits.
            items_read = [ProductoRead.model_validate(item) for item in items]
            logger.info(
                f"Productos paginados: page={page} size={page_size} "
                f"search={search!r} categoria_id={categoria_id} total={total}"
            )
            return PaginatedResponse(
                items       = items_read,
                page        = page,
                page_size   = page_size,
                total_pages = ceil(total / page_size) if total > 0 else 1,
            )

    def update(self, product_id: int, data: ProductoUpdate):
        logger.info(f"Actualizando producto id={product_id}")
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_by_id(product_id)

            if not producto:
                logger.warning(f"Producto id={product_id} no encontrado para update")
                raise HTTPException(404, "Producto no encontrado")
        
            producto.name = data.name
            producto.price = data.price
            producto.stock_cantidad = data.stock_cantidad
            producto.disponible = data.disponible
            producto.imagen_url = data.imagen_url

            viejas_cats = uow.producto_categorias.get_by_producto(product_id)
            for rel in viejas_cats:
                uow.producto_categorias.delete(rel)

            for cat_id in set(data.categorias):
                categoria = uow.categorias.get_by_id(cat_id)
                if not categoria:
                    raise HTTPException(404, f"Categoria {cat_id} no existe")
                uow.producto_categorias.add(
                    ProductoCategoria(
                        producto_id=product_id,
                        categoria_id=cat_id,
                        es_principal=False
                )
            )

        uow._session.refresh(producto)
        return producto

        
    def get_all(self):
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_all()
            if not producto:
                raise HTTPException(404, "No se encontraron productos") 
            return producto
        
    def get_by_id(self, product_id: int):
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_by_id(product_id)
            if not producto:
                raise HTTPException(404, "Producto no encontrado")
            return producto

    def delete(self, product_id: int):
        logger.info(f"Eliminando producto id={product_id}")
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_by_id(product_id)
            if not producto:
                logger.warning(f"Producto id={product_id} no encontrado para delete")
                raise HTTPException(404, "Producto no encontrado")
        
            viejas_cats = uow.producto_categorias.get_by_producto(product_id)
            for rel in viejas_cats:
                uow.producto_categorias.delete(rel)
        
            viejos_ingres = uow.producto_ingredientes.get_by_producto(product_id)
            for rel in viejos_ingres:
                uow.producto_ingredientes.delete(rel)
        
            uow.productos.delete(producto)