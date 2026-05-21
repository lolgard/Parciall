from datetime import datetime
from typing import TYPE_CHECKING
from sqlmodel import Field, Relationship, SQLModel

if TYPE_CHECKING:
    from app.modules.Producto.model import Producto
    from app.modules.ProductoIngredientes.model import ProductoIngrediente
class UnidadDeMedida(SQLModel, table=True):
    __tablename__ = "unidad_medida"
    id: int | None = Field (default = None, primary_key=True)
    name: str
    symbol: str
    type: str

    created_at: datetime = Field(default_factory=datetime.utcnow)
    deleted_at: datetime | None = None


    # MUCHOS productos pueden usar la misma unidad
    productos: list["Producto"] = Relationship(
        back_populates="unidad_medida"
    )

    # MUCHOS productoIngredientes pueden usar la misma unidad
    producto_ingredientes: list["ProductoIngrediente"] = Relationship(
        back_populates="unidad_medida"
    )