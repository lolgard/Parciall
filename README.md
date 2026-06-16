video explicacion 
https://drive.google.com/drive/folders/1VX5V1lqaQgTj-3K96T0uXAvy79Q_gjZd?usp=drive_link
# Backend — Sistema de Ordenes

API REST desarrollada con **FastAPI** y **SQLModel** para gestionar productos, categorías, ingredientes, pedidos y usuarios.

## Stack

- Python 3.13
- FastAPI 0.136
- SQLModel 0.0.38 (SQLAlchemy + Pydantic)
- PostgreSQL (con SSL)
- JWT (python-jose) + bcrypt (passlib)
- Uvicorn

---

## Requisitos previos

- Python 3.11+
- PostgreSQL corriendo (local o remoto)
- pip

---

## Instalación

```bash
# 1. Clonar el repo
git clone https://github.com/lolgard/Parciall.git
cd Parciall

# 2. Crear y activar entorno virtual
python -m venv env
# Windows
env\Scripts\activate
# Linux / Mac
source env/bin/activate

ejemplo: 
.\env\Scripts\python.exe -m uvicorn app.main:app --reload

#en bash
./env/Scripts/python.exe -m uvicorn app.main:app --reload


# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar variables de entorno
cp .env.example .env
# Editar .env con los datos de tu base de datos
```

---

## Variables de entorno

Crear un archivo `.env` en la raíz con:

```env
DATABASE_URL=postgresql://usuario:password@host:5432/nombre_db
SECRET_KEY=una_clave_secreta_minimo_32_caracteres
```

> El archivo `.env` está en `.gitignore` y nunca debe subirse al repo.

---

## Correr el proyecto

```bash
uvicorn app.main:app --reload
```

La API queda disponible en `http://localhost:8000`.

Documentación interactiva: `http://localhost:8000/docs`

---

## Seed (datos iniciales)

Para poblar la base con usuarios, roles, estados de pedido y formas de pago:

```bash
python -m app.db.seed
```

Crea los siguientes usuarios de prueba:

| Usuario | Contraseña | Rol |
|---|---|---|
| admin | Admin1234! | ADMIN |
| cliente | Cliente1234! | CLIENTE |
| cocinero | Cocinero1234! | COCINERO |

También crea: unidades de medida, estados de pedido (PENDIENTE → ENTREGADO) y formas de pago (EFECTIVO, TARJETA, TRANSFERENCIA, MERCADO_PAGO).

---

## Endpoints disponibles

| Método | Ruta | Descripción |
|---|---|---|
| GET | `/` | Health check |
| POST/GET | `/usuarios/` | Crear / listar usuarios |
| GET/PATCH/DELETE | `/usuarios/{id}` | Detalle / editar / eliminar usuario |
| POST/GET | `/productos/` | Crear / listar productos |
| GET/PUT/DELETE | `/productos/{id}` | Detalle / editar / eliminar producto |
| POST/GET | `/categorias/` | Crear / listar categorías |
| GET/PUT/DELETE | `/categorias/{id}` | Detalle / editar / eliminar categoría |
| POST/GET | `/ingredientes/` | Crear / listar ingredientes |
| POST/GET | `/pedidos/` | Crear / listar pedidos |
| GET/PUT/DELETE | `/pedidos/{id}` | Detalle / editar / eliminar pedido |
| POST/GET | `/detalle-pedidos/` | Crear / listar ítems de pedido |
| POST/GET | `/direcciones-entrega/` | Crear / listar direcciones |

---

## Estructura de carpetas

```
app/
├── core/
│   ├── config.py        # Variables de entorno (pydantic-settings)
│   ├── database.py      # Engine y sesión SQLModel
│   ├── deps.py          # Dependencias FastAPI
│   ├── repository.py    # BaseRepository genérico (CRUD)
│   ├── security.py      # Hash bcrypt + JWT
│   └── unit_of_work.py  # BaseUnitOfWork (manejo de transacciones)
├── db/
│   └── seed.py          # Script de datos iniciales
├── modules/
│   ├── Categoria/
│   ├── Ingrediente/
│   ├── Producto/
│   ├── ProductoCategoria/
│   ├── ProductoIngredientes/
│   ├── detallePedido/
│   ├── direccionEntrega/
│   ├── estadoPedido/
│   ├── formaPago/
│   ├── pedido/
│   ├── refreshToken/
│   ├── rol/
│   ├── unidadDeMedida/
│   ├── usuario/
│   └── usuarioRol/
└── main.py              # Punto de entrada, registro de routers y CORS
```

Cada módulo sigue la misma estructura en capas:

```
modulo/
├── model.py       # Tabla SQLModel
├── schema.py      # DTOs de entrada/salida
├── repository.py  # Queries a la DB (extiende BaseRepository)
├── service.py     # Lógica de negocio
├── unit_of_work.py# Gestión de transacción
└── router.py      # Endpoints FastAPI
```

---

## CORS

Configurado para aceptar requests desde `http://localhost:5173` (frontend Vite en desarrollo).

##
```
Estructura de proyecto
app/
├── core/
│   ├── config.py        # Variables de entorno (pydantic-settings)
│   ├── database.py      # Engine y sesión SQLModel
│   ├── deps.py          # Dependencias FastAPI
│   ├── repository.py    # BaseRepository genérico (CRUD)
│   ├── security.py      # Hash bcrypt + JWT
│   └── unit_of_work.py  # BaseUnitOfWork (manejo de transacciones)
├── db/
│   └── seed.py          # Script de datos iniciales
├── modules/
│   ├── Categoria/
│   ├── Ingrediente/
│   ├── Producto/
│   ├── ProductoCategoria/
│   ├── ProductoIngredientes/
│   ├── detallePedido/
│   ├── direccionEntrega/
│   ├── estadoPedido/
│   ├── formaPago/
│   ├── pedido/
│   ├── refreshToken/
│   ├── rol/
│   ├── unidadDeMedida/
│   ├── usuario/
│   └── usuarioRol/
└── main.py              # Punto de entrada, registro de routers y CORS
```
