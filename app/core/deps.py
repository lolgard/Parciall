"""
Dependencias de autenticación y autorización para FastAPI.

Este módulo define funciones que se inyectan con Depends() para:
- Extraer el token JWT desde el request
- Validar autenticación
- Validar estado del usuario
- Validar permisos (roles)

Flujo de ejecución típico:

    Request HTTP
        ↓
    oauth2_scheme → extrae el token Bearer del header Authorization
        ↓
    get_current_user → decodifica el JWT y busca el usuario en DB
        ↓
    get_current_active_user → valida que el usuario esté activo
        ↓
    require_role([...]) → valida permisos (RBAC)

Convenciones HTTP:
    401 → No autenticado (token inválido, ausente o expirado)
    403 → Autenticado pero sin permisos suficientes

Arquitectura:
    - Capa Core (dependencias reutilizables)
    - Depende de:
        * Unit of Work (acceso a datos)
        * Seguridad (JWT)
        * Modelo Usuario
"""

from typing import Annotated  # Permite tipado enriquecido para Depends

from fastapi import Depends, HTTPException, status  # Inyección y manejo de errores HTTP
from fastapi.security import OAuth2PasswordBearer  # Manejo estándar de OAuth2 con Bearer

from app.core.security import decode_access_token  # Función para decodificar JWT
from app.modules.usuario.model  import Usuario     # Modelo de dominio Usuario
from app.modules.usuario.schema import UsuarioRead     # Esquema de lectura de Usuario
from sqlmodel import Session
from app.core.database import get_session
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork

from fastapi import Request

class OAuth2PasswordBearerWithCookie(OAuth2PasswordBearer):
    async def __call__(self, request: Request) -> str | None:
        # 1. Obtener el token EXCLUSIVAMENTE de la cookie (HttpOnly)
        token = request.cookies.get("access_token")
        
        # 2. El soporte para el header Authorization fue deshabilitado.
        # ¿Por qué? Para maximizar la seguridad y forzar el uso de cookies HttpOnly.
        # Las cookies HttpOnly no pueden ser leídas por JavaScript (mitigando ataques XSS).
        # Si permitiéramos usar el token vía header, el frontend tendría que manipular
        # el token en texto plano, arruinando el propósito de la cookie HttpOnly.
        # 
        # if not token:
        #     authorization = request.headers.get("Authorization")
        #     if authorization and authorization.startswith("Bearer "):
        #         token = authorization.split(" ")[1]
                
        if not token:
            if self.auto_error:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="No autenticado",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            else:
                return None
        return token

# Define el esquema OAuth2 que extrae el token de la cookie (o header)
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/api/v1/auth/token")



async def get_current_user(
    token: Annotated[str, Depends(oauth2_scheme)],  # Token extraído automáticamente
    session: Annotated[Session, Depends(get_session)],   # Inyección de Session
):
    """
    Decodifica el JWT y retorna el Usuario correspondiente.

    Responsabilidades:
    - Validar token
    - Extraer identidad (username)
    - Buscar usuario en base de datos
    """

    # Excepción estándar para errores de autenticación (401)
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas o token expirado",
        headers={"WWW-Authenticate": "Bearer"},  # Obligatorio en OAuth2 por protocolo
    )

    # Decodifica el JWT → devuelve payload o None si es inválido
    payload = decode_access_token(token)
    if payload is None:
        raise credentials_exception

    # Extrae el "subject" (usuario) del token
    username: str | None = payload.get("sub")
    if username is None:
        raise credentials_exception

    uow = UsuarioUnitOfWork(session)
    with uow:
        # Busca el usuario en base de datos
        user = uow.usuarios.get_by_username(username)

        # Si no existe el usuario → token inválido
        if user is None:
            raise credentials_exception

        user_read = UsuarioRead.model_validate(user)
        user_read.roles = [r.rol_codigo for r in user.usuarioRol] if user.usuarioRol else []
        return user_read


async def get_current_active_user(
    current_user: Annotated[UsuarioRead, Depends(get_current_user)],
) -> UsuarioRead:
    """
    Verifica que el usuario autenticado esté activo.
    """
    if current_user.deleted_at is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cuenta de usuario desactivada o eliminada",
        )

    return current_user


def require_role(allowed_roles: list[str]):
    """
    Factory de dependencias para control de acceso basado en roles (RBAC).

    Genera dinámicamente una dependencia que valida si el usuario
    tiene uno de los roles permitidos.

    Parámetros:
        allowed_roles → lista de roles válidos (ej: ["ADMIN", "CLIENT"])
    """

    async def role_checker(
        current_user: Annotated[UsuarioRead, Depends(get_current_active_user)],
    ) -> UsuarioRead:
        """
        Valida que el rol del usuario esté dentro de los permitidos.
        """
        # Si ninguno de los roles del usuario está permitido → 403 (prohibido)
        if not any(r in allowed_roles for r in current_user.roles):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=(
                    f"Permisos insuficientes. Tus roles son {current_user.roles}. "
                    f"Se requiere uno de: {allowed_roles}"
                ),
            )

        return current_user  # Usuario autorizado

    return role_checker  # Retorna la dependencia configurada