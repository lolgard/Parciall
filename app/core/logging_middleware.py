import time
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from app.core.logger import get_logger

logger = get_logger("api")


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start = time.perf_counter()
        logger.info(f"-> {request.method} {request.url.path}")

        try:
            response = await call_next(request)
        except Exception as exc:
            elapsed = (time.perf_counter() - start) * 1000
            logger.error(f"X {request.method} {request.url.path} — excepcion no manejada ({elapsed:.0f}ms): {exc}")
            raise

        elapsed = (time.perf_counter() - start) * 1000
        level = logger.warning if response.status_code >= 400 else logger.info
        level(f"<- {response.status_code} {request.method} {request.url.path} ({elapsed:.0f}ms)")

        return response
