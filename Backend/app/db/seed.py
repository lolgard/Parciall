"""
Script de seed — carga usuarios iniciales para pruebas.
Idempotente: se puede ejecutar múltiples veces sin duplicar datos.

Uso:
    python -m app.db.seed

Requiere PostgreSQL corriendo con las variables de .env configuradas.

Crea:
  - admin / Admin1234!  (roles=admin)
  - juan / Juan1234!    (roles=user)
"""

from sqlmodel import Session, select
from app.core.database import engine, create_all_tables
from app.modules.usuario.model import Usuario
from app.core.security import hash_password

USUARIOS_INICIALES = [
    {
        "name":  "admin",
        "lastname": "Administrador del Sistema",
        "email":     "admin@example.com",
        "password_hash":  "Admin1234!",
        "roles":      "admin",
        "phone_number": 1234567890,
    },
  
  
    {
        "name":  "juan",
        "lastname": "Juan Pérez",
        "email":     "juan@example.com",
        "password_hash":  "Juan1234!",
        "roles":      "user",
        "phone_number": 9876543210,
    },
]


def run() -> None:
    print("=== Seed — Seguridad JWT (PostgreSQL) ===")
    create_all_tables()

    with Session(engine) as session:
        for data in USUARIOS_INICIALES:
            existing = session.exec(
                select(Usuario).where(Usuario.name == data["name"])
            ).first()

            if existing:
                print(f"  [=] Ya existe: {data['name']} ({data['roles']})")
            else:
                usuario = Usuario(
                    name            = data["name"],
                    lastname        = data["lastname"],
                    email           = data["email"],
                    password_hash   = hash_password(data["password_hash"]), 
                    roles           = data["roles"],
                    phone_number    = data["phone_number"],
                )
                session.add(usuario)
                print(f"  [+] Creado:    {data['name']} / {data['password_hash']}  (roles={data['roles']})")

        session.commit()

    print("\nUsuarios disponibles para pruebas:")
    print("  admin / Admin1234!  → roles=admin  (acceso total)")
    print("  juan  / Juan1234!   → roles=user   (acceso básico)")
    print()


if __name__ == "__main__":
    run()
