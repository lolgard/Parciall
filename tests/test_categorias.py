"""Tests para el endpoint /categorias/"""

from fastapi.testclient import TestClient


# ── GET /categorias/ ──────────────────────────────────────────────────────────

def test_get_categorias_empty(client: TestClient):
    resp = client.get("/categorias/")
    assert resp.status_code == 200
    assert resp.json() == []


def test_get_categorias_returns_list(client: TestClient):
    client.post("/categorias/", json={"nombre": "Pizzas", "descripcion": "Pizzas artesanales"})
    client.post("/categorias/", json={"nombre": "Bebidas", "descripcion": "Bebidas frias"})

    resp = client.get("/categorias/")
    assert resp.status_code == 200
    data = resp.json()
    assert len(data) == 2
    nombres = {c["nombre"] for c in data}
    assert nombres == {"Pizzas", "Bebidas"}


# ── POST /categorias/ ─────────────────────────────────────────────────────────

def test_create_categoria_ok(client: TestClient):
    payload = {"nombre": "Hamburguesas", "descripcion": "Hamburguesas artesanales"}
    resp = client.post("/categorias/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    assert data["nombre"] == "Hamburguesas"
    assert data["id"] is not None


def test_create_categoria_con_imagen(client: TestClient):
    payload = {
        "nombre": "Postres",
        "descripcion": "Postres del dia",
        "imagen_url": "https://example.com/postres.jpg",
    }
    resp = client.post("/categorias/", json=payload)
    assert resp.status_code == 200
    assert resp.json()["imagen_url"] == "https://example.com/postres.jpg"


def test_create_categoria_sin_imagen(client: TestClient):
    resp = client.post("/categorias/", json={"nombre": "Ensaladas", "descripcion": "Frescas"})
    assert resp.status_code == 200
    assert resp.json()["imagen_url"] is None


# ── GET /categorias/{id} ──────────────────────────────────────────────────────

def test_get_categoria_por_id(client: TestClient):
    created = client.post("/categorias/", json={"nombre": "Pizzas", "descripcion": "Desc"}).json()
    resp = client.get(f"/categorias/{created['id']}")
    assert resp.status_code == 200
    assert resp.json()["nombre"] == "Pizzas"


def test_get_categoria_no_existe(client: TestClient):
    resp = client.get("/categorias/9999")
    assert resp.status_code == 404


# ── PUT /categorias/{id} ──────────────────────────────────────────────────────

def test_update_categoria(client: TestClient):
    created = client.post("/categorias/", json={"nombre": "Viejo", "descripcion": "Vieja"}).json()
    resp = client.put(f"/categorias/{created['id']}", json={"nombre": "Nuevo", "descripcion": "Nueva"})
    assert resp.status_code == 200
    assert resp.json()["nombre"] == "Nuevo"


# ── DELETE /categorias/{id} ───────────────────────────────────────────────────

def test_delete_categoria(client: TestClient):
    created = client.post("/categorias/", json={"nombre": "Temporal", "descripcion": "Borrar"}).json()
    resp = client.delete(f"/categorias/{created['id']}")
    assert resp.status_code == 200

    resp2 = client.get(f"/categorias/{created['id']}")
    assert resp2.status_code == 404
