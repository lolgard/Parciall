import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse

# Diccionario en memoria: { "ip": [timestamp1, timestamp2, ...] }
RATE_LIMIT_STORE = {}

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int = 100, window_seconds: int = 60):
        super().__init__(app)
        self.max_requests = max_requests
        self.window_seconds = window_seconds

    async def dispatch(self, request: Request, call_next):
        # Excluir rutas de websockets si es necesario, o rutas estáticas
        if request.url.path.startswith("/ws"):
            return await call_next(request)

        client_ip = request.client.host if request.client else "unknown"
        current_time = time.time()

        if client_ip not in RATE_LIMIT_STORE:
            RATE_LIMIT_STORE[client_ip] = []

        # Filtrar peticiones que están fuera de la ventana de tiempo
        RATE_LIMIT_STORE[client_ip] = [
            timestamp for timestamp in RATE_LIMIT_STORE[client_ip]
            if current_time - timestamp < self.window_seconds
        ]

        # Comprobar límite
        if len(RATE_LIMIT_STORE[client_ip]) >= self.max_requests:
            return JSONResponse(
                status_code=429,
                content={
                    "detail": "Too Many Requests",
                    "message": "Has excedido el límite de peticiones. Inténtalo más tarde."
                }
            )

        # Añadir petición actual
        RATE_LIMIT_STORE[client_ip].append(current_time)

        # Continuar con la petición
        response = await call_next(request)
        return response
