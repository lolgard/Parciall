from datetime import datetime

from sqlmodel import Session, select

from app.modules.pedido.model import Pedido


class PedidoRepository:
    def __init__(self, session: Session):
        self.session = session

    def add(self, pedido: Pedido) -> Pedido:
        self.session.add(pedido)
        self.session.flush()
        return pedido

    def get_by_id(self, id: int) -> Pedido | None:
        pedido = self.session.get(Pedido, id)
        if not pedido or getattr(pedido, "deleted_at", None) is not None:
            return None
        return pedido

    def get_all(self) -> list[Pedido]:
        return self.session.exec(select(Pedido).where(Pedido.deleted_at == None)).all()

    def get_abandoned(self) -> list[Pedido]:
        from datetime import timedelta
        ahora = datetime.utcnow()
        return self.session.exec(
 # Buscar órdenes PAGO_PENDIENTE antiguas (> 1h)
            query_mp = select(Pedido).where(
                Pedido.estado_codigo == "PAGO_PENDIENTE",
                Pedido.created_at < (ahora - timedelta(hours=1)),
                Pedido.deleted_at == None
            )
            ).all()           
    def get_active_old(self) -> list[Pedido]:
        from datetime import timedelta
        ahora = datetime.utcnow()
        return self.session.exec(
            # Buscar órdenes normales activas antiguas (> 23h)
            query_activas = select(Pedido).where(
                Pedido.estado_codigo.in_(["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"]),
                Pedido.created_at < (ahora - timedelta(hours=23)),
                Pedido.deleted_at == None
            )).all()
    
    def update(self, pedido: Pedido) -> Pedido:
        self.session.add(pedido)
        self.session.flush()
        return pedido

    def delete(self, pedido: Pedido) -> None:
        pedido.deleted_at = datetime.utcnow()
        self.session.add(pedido)

    def get_paginated_by_user(self, user_id: int, estado_filter: str | None, search: str | None, skip: int, limit: int) -> list[Pedido]:
        from sqlalchemy import cast, String
        query = select(Pedido).where(Pedido.deleted_at == None, Pedido.usuario_id == user_id)
        if estado_filter:
            if estado_filter == 'ACTIVOS':
                query = query.where(Pedido.estado_codigo.in_(["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"]))
            elif estado_filter == 'FINALIZADOS':
                query = query.where(Pedido.estado_codigo.in_(["ENTREGADO", "CANCELADO"]))
            else:
                query = query.where(Pedido.estado_codigo == estado_filter)
        
        if search:
            query = query.where(cast(Pedido.id, String).ilike(f"%{search}%"))
                
        # Orden descendente por id (los más recientes primero)
        query = query.order_by(Pedido.id.desc()).offset(skip).limit(limit)
        return self.session.exec(query).all()
        
    def count_by_user(self, user_id: int, estado_filter: str | None, search: str | None) -> int:
        from sqlmodel import func
        from sqlalchemy import cast, String
        query = select(func.count(Pedido.id)).where(Pedido.deleted_at == None, Pedido.usuario_id == user_id)
        if estado_filter:
            if estado_filter == 'ACTIVOS':
                query = query.where(Pedido.estado_codigo.in_(["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"]))
            elif estado_filter == 'FINALIZADOS':
                query = query.where(Pedido.estado_codigo.in_(["ENTREGADO", "CANCELADO"]))
            else:
                query = query.where(Pedido.estado_codigo == estado_filter)
                
        if search:
            query = query.where(cast(Pedido.id, String).ilike(f"%{search}%"))
            
        return self.session.exec(query).one_or_none() or 0
