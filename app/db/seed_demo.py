"""
Seed de datos demo para probar el frontend-store.
Crea categorias, ingredientes y productos directamente via modelos ORM.

Uso:
    python -m app.db.seed_demo
"""

from sqlmodel import Session, select
from app.core.database import engine, create_db_and_tables

# All models must be imported so SQLAlchemy can resolve cross-model relationships
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

DEFAULT_IMAGE = "https://i.ibb.co/RkjRZ7VF/pizza.webp"

CATEGORIAS = [
    {"nombre": "Hamburguesas", "descripcion": "Hamburguesas artesanales"},
    {"nombre": "Pizzas",       "descripcion": "Pizzas al horno de piedra"},
    {"nombre": "Ensaladas",    "descripcion": "Ensaladas frescas y saludables"},
    {"nombre": "Bebidas",      "descripcion": "Bebidas frias y calientes"},
    {"nombre": "Postres",      "descripcion": "Postres caseros del dia"},
]

INGREDIENTES = [
    {"name": "Carne vacuna",    "description": "200g de carne vacuna premium",  "esAlergeno": False},
    {"name": "Queso cheddar",   "description": "Queso cheddar fundido",          "esAlergeno": True},
    {"name": "Lechuga",         "description": "Lechuga fresca",                "esAlergeno": False},
    {"name": "Tomate",          "description": "Tomate natural en rodajas",      "esAlergeno": False},
    {"name": "Cebolla",         "description": "Cebolla caramelizada",           "esAlergeno": False},
    {"name": "Panceta",         "description": "Panceta ahumada crocante",       "esAlergeno": False},
    {"name": "Mozzarella",      "description": "Queso mozzarella fresco",        "esAlergeno": True},
    {"name": "Salsa de tomate", "description": "Salsa de tomate artesanal",      "esAlergeno": False},
    {"name": "Albahaca",        "description": "Albahaca fresca",               "esAlergeno": False},
    {"name": "Gluten de trigo", "description": "Masa con gluten de trigo",       "esAlergeno": True},
]


def run():
    print("=== Seed Demo — datos para frontend-store ===\n")
    create_db_and_tables()

    with Session(engine) as session:

        # ── 1. Unidad de medida ────────────────────────────────────────────────
        unidad = session.exec(
            select(UnidadDeMedida).where(UnidadDeMedida.name == "unidad")
        ).first()
        if not unidad:
            print("  ERROR: unidad de medida 'unidad' no encontrada. Ejecuta seed.py primero.")
            return
        print(f"  Unidad de medida: '{unidad.name}' (id={unidad.id})\n")

        # ── 2. Categorias ──────────────────────────────────────────────────────
        print("-- Categorias --")
        cat_ids: dict[str, int] = {}

        for data in CATEGORIAS:
            existing = session.exec(
                select(Categoria).where(Categoria.nombre == data["nombre"])
            ).first()

            if existing:
                cat_ids[data["nombre"]] = existing.id
                print(f"  =  Ya existe: {data['nombre']} (id={existing.id})")
            else:
                cat = Categoria(imagen_url=DEFAULT_IMAGE, **data)
                session.add(cat)
                session.flush()
                cat_ids[data["nombre"]] = cat.id
                print(f"  +  Creada:    {data['nombre']} (id={cat.id})")

        # ── 3. Ingredientes ────────────────────────────────────────────────────
        print("\n-- Ingredientes --")
        ing_ids: dict[str, int] = {}

        for data in INGREDIENTES:
            existing = session.exec(
                select(Ingrediente).where(Ingrediente.name == data["name"])
            ).first()

            if existing:
                ing_ids[data["name"]] = existing.id
                print(f"  =  Ya existe: {data['name']} (id={existing.id})")
            else:
                ing = Ingrediente(**data)
                session.add(ing)
                session.flush()
                ing_ids[data["name"]] = ing.id
                print(f"  +  Creado:    {data['name']} (id={ing.id})")

        # ── 4. Productos ───────────────────────────────────────────────────────
        print("\n-- Productos --")

        def cat(*names: str) -> list[int]:
            return [cat_ids[n] for n in names if n in cat_ids]

        def ing(*names: str) -> list[int]:
            return [ing_ids[n] for n in names if n in ing_ids]

        PRODUCTOS = [
            {
                "name": "Hamburguesa Clasica",
                "price": 3500.0, "stock_cantidad": 20, "disponible": True,
                "categorias": cat("Hamburguesas"),
                "ingredientes": ing("Carne vacuna", "Lechuga", "Tomate", "Gluten de trigo"),
            },
            {
                "name": "Hamburguesa BBQ con Panceta",
                "price": 4200.0, "stock_cantidad": 15, "disponible": True,
                "categorias": cat("Hamburguesas"),
                "ingredientes": ing("Carne vacuna", "Panceta", "Queso cheddar", "Cebolla", "Gluten de trigo"),
            },
            {
                "name": "Hamburguesa Doble",
                "price": 5500.0, "stock_cantidad": 10, "disponible": True,
                "categorias": cat("Hamburguesas"),
                "ingredientes": ing("Carne vacuna", "Queso cheddar", "Lechuga", "Tomate", "Gluten de trigo"),
            },
            {
                "name": "Pizza Margherita",
                "price": 4800.0, "stock_cantidad": 12, "disponible": True,
                "categorias": cat("Pizzas"),
                "ingredientes": ing("Salsa de tomate", "Mozzarella", "Albahaca", "Gluten de trigo"),
            },
            {
                "name": "Pizza Cuatro Quesos",
                "price": 5600.0, "stock_cantidad": 8, "disponible": True,
                "categorias": cat("Pizzas"),
                "ingredientes": ing("Salsa de tomate", "Mozzarella", "Queso cheddar", "Gluten de trigo"),
            },
            {
                "name": "Ensalada Cesar",
                "price": 2800.0, "stock_cantidad": 25, "disponible": True,
                "categorias": cat("Ensaladas"),
                "ingredientes": ing("Lechuga", "Tomate"),
            },
            {
                "name": "Ensalada Caprese",
                "price": 3200.0, "stock_cantidad": 18, "disponible": True,
                "categorias": cat("Ensaladas"),
                "ingredientes": ing("Tomate", "Mozzarella", "Albahaca"),
            },
            {
                "name": "Gaseosa 500ml",
                "price": 1200.0, "stock_cantidad": 50, "disponible": True,
                "categorias": cat("Bebidas"),
                "ingredientes": [],
            },
            {
                "name": "Agua Mineral",
                "price": 800.0, "stock_cantidad": 60, "disponible": True,
                "categorias": cat("Bebidas"),
                "ingredientes": [],
            },
            {
                "name": "Brownie de Chocolate",
                "price": 1800.0, "stock_cantidad": 15, "disponible": True,
                "categorias": cat("Postres"),
                "ingredientes": ing("Gluten de trigo"),
            },
            {
                "name": "Tiramisu",
                "price": 2200.0, "stock_cantidad": 10, "disponible": True,
                "categorias": cat("Postres"),
                "ingredientes": [],
            },
        ]

        created = skipped = failed = 0

        for data in PRODUCTOS:
            existing = session.exec(
                select(Producto).where(Producto.name == data["name"])
            ).first()

            if existing:
                print(f"  =  Ya existe: {data['name']}")
                skipped += 1
                continue

            if not data["categorias"]:
                print(f"  !  Sin categoria: {data['name']} (omitido)")
                failed += 1
                continue

            producto = Producto(
                name=data["name"],
                price=data["price"],
                stock_cantidad=data["stock_cantidad"],
                disponible=data["disponible"],
                unidad_medida_id=unidad.id,
            )
            session.add(producto)
            session.flush()

            for cat_id in data["categorias"]:
                session.add(ProductoCategoria(
                    producto_id=producto.id,
                    categoria_id=cat_id,
                    es_principal=False,
                ))

            for ing_id in data["ingredientes"]:
                session.add(ProductoIngrediente(
                    producto_id=producto.id,
                    ingrediente_id=ing_id,
                    unidad_medida_id=unidad.id,
                ))

            print(f"  +  Creado:    {data['name']} (id={producto.id})")
            created += 1

        session.commit()

    print(f"\n-- Resumen --")
    print(f"  Categorias  : {len(cat_ids)}")
    print(f"  Ingredientes: {len(ing_ids)}")
    print(f"  Creados     : {created}")
    print(f"  Ya existian : {skipped}")
    print(f"  Fallidos    : {failed}")


if __name__ == "__main__":
    run()
