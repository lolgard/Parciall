from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork

from app.modules.Producto.repository import (
    ProductoRepository,
    ProductoCategoriaRepository,
    ProductoIngredienteRepository
)

from app.modules.Categoria.repository import CategoriaRepository
from app.modules.Ingrediente.repository import IngredienteRepository


class ProductoUnitOfWork(BaseUnitOfWork):

    def __init__(self, session: Session) -> None:

        super().__init__(session)

        self.productos = ProductoRepository(session)

        self.categorias = CategoriaRepository(session)

        self.ingredientes = IngredienteRepository(session)

        self.producto_categorias = (
            ProductoCategoriaRepository(session)
        )

        self.producto_ingredientes = (
            ProductoIngredienteRepository(session)
        )