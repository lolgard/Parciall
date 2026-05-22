"""
Script de seed — carga usuarios iniciales para pruebas.
Idempotente: se puede ejecutar múltiples veces sin duplicar datos.

Uso:
    python -m app.db.seed

Requiere PostgreSQL corriendo con las variables de .env configuradas.

Crea:
  - admin     / Admin1234!    (rol=ADMIN)
  - cliente   / Cliente1234!  (rol=CLIENTE)
  - cocinero  / Cocinero1234! (rol=COCINERO)
"""

from datetime import datetime, timedelta
from sqlmodel import Session, select
from app.core.database import engine, create_db_and_tables
from app.modules.usuario.model import Usuario
from app.modules.rol.model import Rol
from app.modules.usuarioRol.model import UsuarioRol
from app.core.security import hash_password
from app.modules.unidadDeMedida.model import UnidadDeMedida
from app.modules.refreshToken.model import RefreshToken
from app.modules.direccionEntrega.model import DireccionEntrega
from app.modules.Producto.model import Producto
from app.modules.Categoria.model import Categoria
from app.modules.Ingrediente.model import Ingrediente
from app.modules.ProductoCategoria.model import ProductoCategoria
from app.modules.ProductoIngredientes.model import ProductoIngrediente



# ── Roles ─────────────────────────────────────────────────────────────────────

ROLES_INICIALES = [
    {
        "code":       "ADMIN",
        "name":       "Administrador",
        "descripcion": "Acceso total al sistema.",
    },
    {
        "code":       "CLIENTE",
        "name":       "Cliente",
        "descripcion": "Puede realizar y consultar sus pedidos.",
    },
    {
        "code":       "COCINERO",
        "name":       "Cocinero",
        "descripcion": "Gestiona y prepara los pedidos en cocina.",
    },
]

# ── Usuarios ──────────────────────────────────────────────────────────────────

USUARIOS_INICIALES = [
    {
        "name":          "admin",
        "lastname":      "Administrador del Sistema",
        "email":         "admin@example.com",
        "password_hash": "Admin1234!",
        "phone_number":  123456789,
        "rol_code":      "ADMIN",
    },
    {
        "name":          "cliente",
        "lastname":      "Cliente de Prueba",
        "email":         "cliente@example.com",
        "password_hash": "Cliente1234!",
        "phone_number":  111111111,
        "rol_code":      "CLIENTE",
    },
    {
        "name":          "cocinero",
        "lastname":      "Cocinero de Prueba",
        "email":         "cocinero@example.com",
        "password_hash": "Cocinero1234!",
        "phone_number":  222222222,
        "rol_code":      "COCINERO",
    },
]

# ── Unidades de medida ────────────────────────────────────────────────────────

UNIDADES_INICIALES = [
    {"name": "gramo",     "symbol": "g",   "type": "masa"},
    {"name": "kilogramo", "symbol": "kg",  "type": "masa"},
    {"name": "mililitro", "symbol": "ml",  "type": "volumen"},
    {"name": "litro",     "symbol": "l",   "type": "volumen"},
    {"name": "docena",    "symbol": "doc", "type": "unidad"},
    {"name": "unidad",    "symbol": "un",  "type": "unidad"},
]


# ── Runner ────────────────────────────────────────────────────────────────────

def run() -> None:
    print("=== Seed — Seguridad JWT (PostgreSQL) ===\n")
    create_db_and_tables()

    with Session(engine) as session:

        # 1. Roles
        print("-- Roles --")
        for data in ROLES_INICIALES:
            existing = session.exec(
                select(Rol).where(Rol.code == data["code"])
            ).first()

            if existing:
                print(f"  [=] Ya existe: {data['code']}")
            else:
                rol = Rol(**data)
                session.add(rol)
                print(f"  [+] Creado:    {data['code']} — {data['name']}")

        session.flush()  # IDs disponibles antes de asignar relaciones

        # 2. Usuarios + asignación de rol
        print("\n-- Usuarios --")
        expires = datetime.utcnow() + timedelta(days=365)

        for data in USUARIOS_INICIALES:
            existing = session.exec(
                select(Usuario).where(Usuario.name == data["name"])
            ).first()

            if existing:
                print(f"  [=] Ya existe: {data['name']} ({data['rol_code']})")
                continue

            usuario = Usuario(
                name          = data["name"],
                lastname      = data["lastname"],
                email         = data["email"],
                password_hash = hash_password(data["password_hash"]),
                phone_number  = data["phone_number"],
            )
            session.add(usuario)
            session.flush()  # obtener usuario.id antes de crear UsuarioRol

            rol = session.exec(
                select(Rol).where(Rol.code == data["rol_code"])
            ).first()

            usuario_rol = UsuarioRol(
                usuario_id  = usuario.id,
                rol_codigo  = rol.code,
                create_at   = datetime.utcnow(),
                expires_at  = expires,
            )
            session.add(usuario_rol)
            print(f"  [+] Creado:    {data['name']} / {data['password_hash']}  (rol={data['rol_code']})")

        # 3. Unidades de medida
        print("\n-- Unidades de medida --")
        for data in UNIDADES_INICIALES:
            existing = session.exec(
                select(UnidadDeMedida).where(UnidadDeMedida.name == data["name"])
            ).first()

            if existing:
                print(f"  [=] Ya existe: {data['name']}")
            else:
                session.add(UnidadDeMedida(**data))
                print(f"  [+] Creada:    {data['name']} ({data['symbol']})")

        session.commit()

    print("\n=== Credenciales de prueba ===")
    print("  admin    / Admin1234!    → ADMIN")
    print("  cliente  / Cliente1234!  → CLIENTE")
    print("  cocinero / Cocinero1234! → COCINERO")
    print()


if __name__ == "__main__":
    run()