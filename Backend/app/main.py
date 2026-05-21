from fastapi import FastAPI
from app.core.database import create_db_and_tables
from fastapi.middleware.cors import CORSMiddleware

# Importar modelos para que SQLAlchemy los registre
import app.modules.refreshToken.model
import app.modules.rol.model

# Routers
from app.modules.Producto.router import router as producto_router
from app.modules.Categoria.router import router as categoria_router
from app.modules.Ingrediente.router import router as ingrediente_router
from app.modules.direccionEntrega.router import router as direccion_entrega_router
from app.modules.usuario.router import router as usuario_router

#crea la app
app = FastAPI(
    title="Sistema de Ordenes",
    version="1.0.0"
)
#cords
origins = [
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas al iniciar (opcional en dev)
@app.on_event("startup")
def on_startup():
    create_db_and_tables()


#  Registrar routers
app.include_router(producto_router)
app.include_router(categoria_router)
app.include_router(ingrediente_router)

app.include_router(direccion_entrega_router)
app.include_router(usuario_router)

@app.get("/")
def root():
    return {"message": "API funcionando 🚀"}