"""
Fixtures compartidas para los tests de API.
Usa una base de datos SQLite en memoria aislada por sesión de tests.
"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import SQLModel, Session, create_engine
from sqlmodel.pool import StaticPool

from app.main import app
from app.core.database import get_session

# Importar todos los modelos para que SQLAlchemy resuelva relaciones
from app.modules.refreshToken.model import RefreshToken
from app.modules.rol.model import Rol
from app.modules.usuarioRol.model import UsuarioRol
from app.modules.usuario.model import Usuario
from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.pedido.model import Pedido
from app.modules.detallePedido.model import DetallePedido
from app.modules.estadoPedido.model import EstadoPedido
from app.modules.formaPago.model import FormaPago
from app.modules.Categoria.model import Categoria
from app.modules.Ingrediente.model import Ingrediente
from app.modules.Producto.model import Producto
from app.modules.ProductoCategoria.model import ProductoCategoria
from app.modules.ProductoIngredientes.model import ProductoIngrediente
from app.modules.unidadDeMedida.model import UnidadDeMedida


@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite:///:memory:",
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session
    SQLModel.metadata.drop_all(engine)


from app.core.deps import get_current_user, get_current_active_user
from app.modules.usuario.schema import UsuarioRead

@pytest.fixture(name="client")
def client_fixture(session: Session):
    def override_get_session():
        yield session

    mock_admin = UsuarioRead(
        id=999,
        email="test_admin@example.com",
        name="Test",
        lastname="Admin",
        roles=["ADMIN"]
    )

    app.dependency_overrides[get_session] = override_get_session
    app.dependency_overrides[get_current_user] = lambda: mock_admin
    app.dependency_overrides[get_current_active_user] = lambda: mock_admin
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()


@pytest.fixture(name="unidad_id")
def unidad_fixture(session: Session) -> int:
    unidad = UnidadDeMedida(name="unidad", symbol="un", type="unidad")
    session.add(unidad)
    session.commit()
    session.refresh(unidad)
    return unidad.id


@pytest.fixture(name="categoria_id")
def categoria_fixture(session: Session) -> int:
    cat = Categoria(nombre="Test", descripcion="Categoria de prueba")
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat.id
