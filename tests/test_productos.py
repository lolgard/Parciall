"""Tests para el endpoint /productos/"""

from fastapi.testclient import TestClient


def _producto_base(unidad_id: int, categoria_id: int, **kwargs) -> dict:
    return {
        "name": "Producto Test",
        "price": 1500.0,
        "stock_cantidad": 10,
        "disponible": True,
        "unidad_medida_id": unidad_id,
        "categorias": [categoria_id],
        "ingredientes": [],
        **kwargs,
    }


# ── GET /productos/ ───────────────────────────────────────────────────────────

def test_get_productos_paginado_vacio(client: TestClient):
    resp = client.get("/productos/")
    assert resp.status_code == 200
    data = resp.json()
    assert data["items"] == []
    assert data["page"] == 1


def test_get_productos_paginado(client: TestClient, unidad_id: int, categoria_id: int):
    for i in range(3):
        client.post("/productos/", json=_producto_base(unidad_id, categoria_id, name=f"Prod {i}"))

    resp = client.get("/productos/?page=1&page_size=10")
    assert resp.status_code == 200
    assert len(resp.json()["items"]) == 3


def test_paginacion_page_size(client: TestClient, unidad_id: int, categoria_id: int):
    for i in range(5):
        client.post("/productos/", json=_producto_base(unidad_id, categoria_id, name=f"Prod {i}"))

    resp = client.get("/productos/?page=1&page_size=2")
    assert resp.status_code == 200
    assert len(resp.json()["items"]) == 2


# ── POST /productos/ ──────────────────────────────────────────────────────────

def test_create_producto_ok(client: TestClient, unidad_id: int, categoria_id: int):
    payload = _producto_base(unidad_id, categoria_id, name="Pizza Margherita", price=4800.0)
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["name"] == "Pizza Margherita"
    assert data["price"] == 4800.0
    assert data["id"] is not None


def test_create_producto_sin_categoria_falla(client: TestClient, unidad_id: int):
    payload = {
        "name": "Sin categoria",
        "price": 1000.0,
        "stock_cantidad": 5,
        "disponible": True,
        "unidad_medida_id": unidad_id,
        "categorias": [],
        "ingredientes": [],
    }
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 400


def test_create_producto_nombre_vacio_falla(client: TestClient, unidad_id: int, categoria_id: int):
    payload = _producto_base(unidad_id, categoria_id, name="   ")
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 400


def test_create_producto_precio_negativo_falla(client: TestClient, unidad_id: int, categoria_id: int):
    payload = _producto_base(unidad_id, categoria_id, price=-100.0)
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 400


def test_create_producto_nombre_duplicado_falla(client: TestClient, unidad_id: int, categoria_id: int):
    payload = _producto_base(unidad_id, categoria_id, name="Mismo nombre")
    client.post("/productos/", json=payload)
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 400


def test_create_producto_categoria_inexistente_falla(client: TestClient, unidad_id: int):
    payload = _producto_base(unidad_id, 9999)
    resp = client.post("/productos/", json=payload)
    assert resp.status_code == 404


# ── GET /productos/{id} ───────────────────────────────────────────────────────

def test_get_producto_por_id(client: TestClient, unidad_id: int, categoria_id: int):
    created = client.post("/productos/", json=_producto_base(unidad_id, categoria_id)).json()
    resp = client.get(f"/productos/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["id"] == created["id"]


def test_get_producto_no_existe(client: TestClient):
    resp = client.get("/productos/9999")
    assert resp.status_code == 404


# ── PUT /productos/{id} ───────────────────────────────────────────────────────

def test_update_producto(client: TestClient, unidad_id: int, categoria_id: int):
    created = client.post("/productos/", json=_producto_base(unidad_id, categoria_id, name="Original")).json()
    payload = _producto_base(unidad_id, categoria_id, name="Actualizado", price=9999.0)
    resp = client.put(f"/productos/{created['id']}", json=payload)
    assert resp.status_code == 200
    assert resp.json()["name"] == "Actualizado"
    assert resp.json()["price"] == 9999.0


# ── DELETE /productos/{id} ────────────────────────────────────────────────────

def test_delete_producto(client: TestClient, unidad_id: int, categoria_id: int):
    created = client.post("/productos/", json=_producto_base(unidad_id, categoria_id)).json()
    resp = client.delete(f"/productos/{created['id']}")
    assert resp.status_code == 200

    resp2 = client.get(f"/productos/{created['id']}")
    assert resp2.status_code == 404
