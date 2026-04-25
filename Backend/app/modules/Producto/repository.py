from fastapi import HTTPException

from app.core.repository import BaseRepository
from app.modules.Producto.model import Producto
from app.modules.ProductoCategoria.model import ProductoCategoria
from sqlmodel import Session, select

from app.modules.ProductoIngredientes.model import ProductoIngrediente
class ProductoRepository(BaseRepository):
    def __init__(self,session:Session):
        self.session = session 
        
    def create(self, data):

        with self.uow as uow:

            # 1. validar que venga categoria
            if not data.categoria_id:
                raise HTTPException(
                    status_code=400,
                    detail="El producto debe tener una categoría"
                )

            # 2. validar que exista en DB
            categoria = uow.categorias.get_by_id(data.categoria_id)

            if not categoria:
                raise HTTPException(
                    status_code=404,
                    detail="La categoría no existe"
                )

            #3. crear producto
            producto = Producto(**data.dict())
            producto = uow.productos.add(producto)

            return producto

    def get_by_name(self,name:str)-> Producto:
        return self.session.exec(
            select(Producto).where(Producto.name == name)
        ).first()
    def get_by_id(self, id: int) -> Producto:
        producto = self.session.get(Producto, id)
        if producto:
            self.session.refresh(producto)
        return producto


    def get_all(self) -> list[Producto]:
        productos = self.session.exec(select(Producto)).all()
        for producto in productos:
            self.session.refresh(producto)
        return productos

    def update(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.flush()
        return producto

    def add(self, producto: Producto) -> Producto:
        self.session.add(producto)
        self.session.flush()
        return producto

    def delete(self,producto:Producto)-> None:
     self.session.delete(producto)

     #--------------------------------repositoryde producto categoria----------------------------
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