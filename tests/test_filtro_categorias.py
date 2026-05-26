"""
Tests para verificar que el endpoint GET /productos/ serializa correctamente
las categorías de cada producto, condición necesaria para que el filtro
client-side del frontend funcione.

Bug corregido: SQLModel table-model .dict() devuelve None para relationship
fields aunque estén cargados. La serialización correcta requiere llamar
ProductoRead.model_validate(orm_obj) mientras la sesión está activa.
"""

import pytest
from fastapi.testclient import TestClient
from sqlmodel import Session

from app.modules.Categoria.model import Categoria


# ── Fixtures adicionales ──────────────────────────────────────────────────────

@pytest.fixture
def cat_pizzas(session: Session) -> int:
    cat = Categoria(nombre="Pizzas", descripcion="Pizzas al horno")
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat.id


@pytest.fixture
def cat_hamburguesas(session: Session) -> int:
    cat = Categoria(nombre="Hamburguesas", descripcion="Hamburguesas artesanales")
    session.add(cat)
    session.commit()
    session.refresh(cat)
    return cat.id


def _payload(unidad_id: int, categoria_ids: list[int], **kwargs) -> dict:
    return {
        "name": "Producto Test",
        "price": 1500.0,
        "stock_cantidad": 10,
        "disponible": True,
        "unidad_medida_id": unidad_id,
        "categorias": categoria_ids,
        "ingredientes": [],
        **kwargs,
    }


# ── Tests de serialización de categorias ─────────────────────────────────────

def test_listado_incluye_categorias_no_nulo(
    client: TestClient, unidad_id: int, cat_pizzas: int
):
    """categorias nunca debe ser null en la respuesta del listado."""
    client.post("/productos/", json=_payload(unidad_id, [cat_pizzas], name="Pizza Test"))

    resp = client.get("/productos/")
    assert resp.status_code == 200
    items = resp.json()["items"]
    assert len(items) == 1
    assert items[0]["categorias"] is not None, (
        "categorias fue None — la serialización de ORM relationships falló"
    )


def test_listado_categoria_id_correcto(
    client: TestClient, unidad_id: int, cat_pizzas: int
):
    """El categoria_id devuelto debe coincidir con el de la categoría asignada."""
    client.post("/productos/", json=_payload(unidad_id, [cat_pizzas], name="Pizza Margherita"))

    resp = client.get("/productos/")
    items = resp.json()["items"]
    categorias = items[0]["categorias"]

    assert len(categorias) == 1
    assert categorias[0]["categoria_id"] == cat_pizzas


def test_listado_categorias_no_vacio(
    client: TestClient, unidad_id: int, cat_hamburguesas: int
):
    """La lista de categorias debe tener al menos un elemento por producto."""
    client.post("/productos/", json=_payload(unidad_id, [cat_hamburguesas], name="Burger"))

    items = client.get("/productos/").json()["items"]
    assert len(items[0]["categorias"]) > 0


def test_listado_multiples_productos_diferentes_categorias(
    client: TestClient, unidad_id: int, cat_pizzas: int, cat_hamburguesas: int
):
    """Cada producto debe exponer su propia categoría, no la de otro."""
    client.post("/productos/", json=_payload(unidad_id, [cat_pizzas], name="Pizza"))
    client.post("/productos/", json=_payload(unidad_id, [cat_hamburguesas], name="Burger"))

    items = client.get("/productos/?page_size=10").json()["items"]
    assert len(items) == 2

    by_name = {p["name"]: p for p in items}
    assert by_name["Pizza"]["categorias"][0]["categoria_id"] == cat_pizzas
    assert by_name["Burger"]["categorias"][0]["categoria_id"] == cat_hamburguesas


def test_listado_producto_multiples_categorias(
    client: TestClient, unidad_id: int, cat_pizzas: int, cat_hamburguesas: int
):
    """Un producto asignado a varias categorías debe exponer todas."""
    client.post(
        "/productos/",
        json=_payload(unidad_id, [cat_pizzas, cat_hamburguesas], name="Especial"),
    )

    items = client.get("/productos/").json()["items"]
    cat_ids = {c["categoria_id"] for c in items[0]["categorias"]}
    assert cat_pizzas in cat_ids
    assert cat_hamburguesas in cat_ids


def test_detalle_producto_incluye_categorias(
    client: TestClient, unidad_id: int, cat_pizzas: int
):
    """GET /productos/{id} también debe devolver categorias correctamente."""
    created = client.post(
        "/productos/", json=_payload(unidad_id, [cat_pizzas], name="Pizza Detail")
    ).json()

    resp = client.get(f"/productos/{created['id']}")
    assert resp.status_code == 200
    categorias = resp.json()["categorias"]
    assert categorias is not None
    assert len(categorias) == 1
    assert categorias[0]["categoria_id"] == cat_pizzas


# ── Test que documenta el bug original ───────────────────────────────────────

def test_categorias_sobreviven_commit(
    client: TestClient, unidad_id: int, cat_pizzas: int
):
    """
    Regresión: SQLModel ORM table-model.dict() devuelve None para campos de
    relación aunque estén cargados con selectinload. La serialización debe
    hacerse con model_validate() dentro de la sesión activa.
    """
    client.post("/productos/", json=_payload(unidad_id, [cat_pizzas], name="Regresion"))

    resp = client.get("/productos/")
    item = resp.json()["items"][0]

    assert item["categorias"] is not None, (
        "Regresión detectada: categorias=null. "
        "Asegurate de usar ProductoRead.model_validate() en el servicio."
    )
    assert item["categorias"][0]["categoria_id"] == cat_pizzas


def test_sin_stock_categoria_presente(
    client: TestClient, unidad_id: int, cat_hamburguesas: int
):
    """Productos sin stock también deben exponer su categoría."""
    client.post(
        "/productos/",
        json=_payload(unidad_id, [cat_hamburguesas], name="Sin Stock", stock_cantidad=0, disponible=False),
    )

    items = client.get("/productos/").json()["items"]
    assert items[0]["categorias"][0]["categoria_id"] == cat_hamburguesas
