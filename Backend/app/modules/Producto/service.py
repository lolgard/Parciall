

from sqlmodel import Session

from app.modules.Producto.unit_of_work import ProductoUnitOfWork
from fastapi import HTTPException

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.Producto.model import Producto
from app.modules.Producto.schema import ProductoCreate
from app.modules.ProductoCategoria.model import ProductoCategoria
from app.modules.ProductoIngredientes.model import ProductoIngrediente

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
                           ingrediente_id=ingre_id
                       )
                   )
            
            return producto

    def update(self, product_id: int, data: ProductoCreate):
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_by_id(product_id)

            if not producto:
                 raise HTTPException(404, "Producto no encontrado")
        
            producto.name = data.name
            producto.price = data.price
            producto.stock_cantidad = data.stock_cantidad
            producto.disponible = data.disponible

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
        with ProductoUnitOfWork(self._session) as uow:
            producto = uow.productos.get_by_id(product_id)
            if not producto:
                raise HTTPException(404, "Producto no encontrado")
        
            viejas_cats = uow.producto_categorias.get_by_producto(product_id)
            for rel in viejas_cats:
                uow.producto_categorias.delete(rel)
        
            viejos_ingres = uow.producto_ingredientes.get_by_producto(product_id)
            for rel in viejos_ingres:
                uow.producto_ingredientes.delete(rel)
        
            uow.productos.delete(producto)