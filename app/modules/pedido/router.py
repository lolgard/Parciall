from fastapi import APIRouter, Depends, Request, WebSocket, WebSocketDisconnect
import json
from sqlmodel import Session
from app.core.database import engine
from app.core.security import decode_access_token
from app.modules.usuario.unit_of_work import UsuarioUnitOfWork
from app.core.websocket import manager

from app.core.database import get_session
from app.modules.pedido.service import PedidoService
from app.modules.pedido.schema import PedidoCreate, PedidoRead, PedidoConDetallesRead, PedidoUpdate
from app.core.deps import get_current_active_user, require_role
from app.modules.usuario.schema import UsuarioRead
from app.modules.pedido.unit_of_work import PedidoUnitOfWork

router = APIRouter(prefix="/pedidos", tags=["pedidos"])


def get_service(session=Depends(get_session)):
    uow = PedidoUnitOfWork(session)
    return PedidoService(uow)


@router.post("/", response_model=PedidoRead)
async def create_pedido(
    data: PedidoCreate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return await service.create(data, current_user.id)


@router.get("/", response_model=list[PedidoConDetallesRead])
async def get_all(
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return await service.get_all(current_user)


@router.get("/{id}", response_model=PedidoConDetallesRead)
def get_by_id(
    id: int,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return service.get_by_id(id, current_user)


@router.put("/{id}", response_model=PedidoRead)
async def update_pedido(
    id: int,
    data: PedidoUpdate,
    current_user: UsuarioRead = Depends(get_current_active_user),
    service: PedidoService = Depends(get_service)
):
    return await service.update(id, data, current_user)


@router.delete("/{id}", dependencies=[Depends(require_role(["ADMIN"]))])
def delete_pedido(
    id: int,
    service: PedidoService = Depends(get_service)
):
    return service.delete(id)


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    token = websocket.query_params.get("token")
    if not token:
        token = websocket.cookies.get("access_token")
        
    if not token:
        await websocket.accept()
        await websocket.close(code=1008, reason="Token de autenticación requerido")
        return

    payload = decode_access_token(token)
    if not payload:
        await websocket.accept()
        await websocket.close(code=1008, reason="Token inválido o expirado")
        return

    user_id_str = payload.get("sub")
    if not user_id_str:
        await websocket.accept()
        await websocket.close(code=1008, reason="Token inválido")
        return

    with Session(engine) as db_session:
        with UsuarioUnitOfWork(db_session) as uow:
            user = uow.usuarios.get_by_id(int(user_id_str))
            if not user or user.deleted_at:
                await websocket.accept()
                await websocket.close(code=1008, reason="Usuario inválido o inactivo")
                return
            
            roles = [r.rol_codigo for r in user.usuarioRol] if user.usuarioRol else []
            user_role = "client"
            if "ADMIN" in roles:
                user_role = "admin"
            elif "PEDIDOS" in roles:
                user_role = "pedidos"
            elif "STOCK" in roles:
                user_role = "cocina"
            user_id = user.id

    await manager.connect(websocket, role=user_role, user_id=user_id)

    if user_role == "admin":
        manager._join_room(websocket, "role:pedidos")
        manager._join_room(websocket, "role:cocina")

    try:
        while True:
            raw = await websocket.receive_text()
            try:
                msg = json.loads(raw)
            except json.JSONDecodeError:
                continue

            action = msg.get("action")
            
            if action == "subscribe-order":
                order_id = msg.get("order_id")
                if not order_id or not isinstance(order_id, int):
                    continue

                if user_role not in ("admin", "pedidos", "cocina"):
                    with Session(engine) as db_session:
                        with PedidoUnitOfWork(db_session) as pedido_uow:
                            pedido = pedido_uow.pedidos.get_by_id(order_id)
                            if not pedido or pedido.usuario_id != user_id:
                                await websocket.send_json({
                                    "event": "ERROR",
                                    "data": {"detail": "No autorizado para este pedido"}
                                })
                                continue

                manager.join_order_room(websocket, order_id)
                await websocket.send_json({
                    "event": "SUBSCRIBED",
                    "data": {"order_id": order_id}
                })

            elif action == "unsubscribe-order":
                order_id = msg.get("order_id")
                if order_id and isinstance(order_id, int):
                    manager.leave_order_room(websocket, order_id)

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception:
        manager.disconnect(websocket)
