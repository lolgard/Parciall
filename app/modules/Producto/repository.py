from datetime import datetime

from fastapi import HTTPException

from sqlalchemy import select as sa_select, func as sa_func
from sqlalchemy.orm import selectinload

from app.core.repository import BaseRepository
from app.modules.Producto.model import Producto
from app.modules.ProductoCategoria.model import ProductoCategoria
from sqlmodel import Session, func, select

from app.modules.ProductoIngredientes.model import ProductoIngrediente
class ProductoRepository(BaseRepository):
    def __init__(self,session:Session):
        self.session = session 
        
    def create(self, data):
            
             #3. crear producto
            producto = Producto(**data.dict())
            producto = self.session.add(producto)

            return producto

    def get_by_name(self,name:str)-> Producto:
        return self.session.exec(
            select(Producto).where(Producto.name == name)
        ).first()
    
    def get_by_id(self, id: int, include_inactivos: bool = False) -> Producto | None:
        producto = self.session.get(Producto, id)

        if not producto:
            return None
        if not include_inactivos and producto.deleted_at is not None:
            return None

        return producto

    def get_all(self, include_inactivos: bool = False) -> list[Producto]:
        q = select(Producto)
        if not include_inactivos:
            q = q.where(Producto.deleted_at == None)
        productos = self.session.exec(q).all()
        for producto in productos:
            self.session.refresh(producto)
        return productos
    
    def get_paginated(
        self,
        offset: int,
        limit: int,
        search: str | None = None,
        categoria_id: int | None = None,
        disponible: bool | None = None,
        stock_status: str | None = None,
        include_inactivos: bool = False,
    ) -> tuple[list[Producto], int]:
        q = sa_select(Producto).order_by(Producto.id.asc())
        if not include_inactivos:
            q = q.where(Producto.deleted_at == None)

        if search:
            q = q.where(Producto.name.ilike(f"%{search}%"))

        if categoria_id is not None:
            q = q.join(
                ProductoCategoria,
                Producto.id == ProductoCategoria.producto_id,
            ).where(ProductoCategoria.categoria_id == categoria_id)

        if disponible is not None:
            q = q.where(Producto.disponible == disponible)
            
        if stock_status == "agotado":
            q = q.where(Producto.stock_cantidad == 0)
        elif stock_status == "bajo":
            q = q.where(Producto.stock_cantidad > 0, Producto.stock_cantidad <= 5)

        total = self.session.execute(
            sa_select(sa_func.count()).select_from(q.subquery())
        ).scalar_one()

        items = list(
            self.session.execute(
                q.options(selectinload(Producto.categorias)).offset(offset).limit(limit)
            ).scalars().all()
        )
        return items, total

    def update(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.flush()
        self.session.refresh(producto)
        return producto

    def add(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.flush()
        return producto

    def delete(self,producto:Producto)-> None:
     producto.deleted_at = datetime.utcnow()
     self.session.add(producto)
     #--------------------------------repository de producto categoria----------------------------
     from app.modules.ProductoCategoria.model import ProductoCategoria
     from sqlmodel import Session, select
class ProductoCategoriaRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, rel: ProductoCategoria):
        self.session.add(rel)
        return rel
#obtenemos las categorias de un producto
    def get_by_producto(self, producto_id: int) -> list[ProductoCategoria]:
        return self.session.exec(
            select(ProductoCategoria).where(
                ProductoCategoria.producto_id == producto_id
            )
        ).all()
     #obtenemos los productos de una categoria
    def get_by_categoria(self, categoria_id: int) -> list[ProductoCategoria]:
        return self.session.exec(
            select(ProductoCategoria).where(
                ProductoCategoria.categoria_id == categoria_id
            )
        ).all()
    

     #  cambiar categoría principal
    def set_principal(self, product_id: int, categoria_id: int):
        relaciones = self.get_by_producto(product_id)

        for r in relaciones:
            r.es_principal = (r.categoria_id == categoria_id)

        return relaciones
    
    def delete(self, rel: ProductoCategoria):
        self.session.delete(rel)
    #--------------------------------repositoryde producto ingrediente----------------------------
    
class ProductoIngredienteRepository(BaseRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, rel: ProductoIngrediente):
        self.session.add(rel)
        return rel

    def get_by_producto(self, producto_id: int) -> list[ProductoIngrediente]:
        return self.session.exec(
            select(ProductoIngrediente).where(
                ProductoIngrediente.producto_id == producto_id
            )
        ).all()

    def delete(self, rel: ProductoIngrediente):
        self.session.delete(rel)
    
    
    