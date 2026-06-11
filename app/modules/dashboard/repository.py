"""
DashboardRepository
===================
Repositorio de solo lectura para el módulo Dashboard.

Centraliza todas las queries analíticas (KPIs, gráficos) en
un único lugar, desacoplando el acceso a datos del servicio.
"""
from datetime import datetime
from sqlmodel import Session, select, func
from app.modules.pedido.model import Pedido
from app.modules.detallePedido.model import DetallePedido
from app.modules.Producto.model import Producto


class DashboardRepository:
    def __init__(self, session: Session):
        self.session = session

    # ── KPIs ──────────────────────────────────────────────────────────────────

    def get_revenue(self, start_dt: datetime, end_dt: datetime) -> float:
        """Recaudación total de pedidos ENTREGADO en el rango de fechas."""
        stmt = select(func.sum(Pedido.total)).where(
            Pedido.estado_codigo == "ENTREGADO",
            Pedido.created_at >= start_dt,
            Pedido.created_at < end_dt,
        )
        return self.session.exec(stmt).one_or_none() or 0.0

    def get_completed_orders_count(self, start_dt: datetime, end_dt: datetime) -> int:
        """Cantidad de pedidos ENTREGADO en el rango de fechas."""
        stmt = select(func.count(Pedido.id)).where(
            Pedido.estado_codigo == "ENTREGADO",
            Pedido.created_at >= start_dt,
            Pedido.created_at < end_dt,
        )
        return self.session.exec(stmt).one_or_none() or 0

    def get_pending_orders_count(self, start_dt: datetime, end_dt: datetime) -> int:
        """Cantidad de pedidos activos (no finalizados) en el rango de fechas."""
        estados_activos = ["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"]
        stmt = select(func.count(Pedido.id)).where(
            Pedido.estado_codigo.in_(estados_activos),
            Pedido.created_at >= start_dt,
            Pedido.created_at < end_dt,
        )
        return self.session.exec(stmt).one_or_none() or 0

    def get_low_stock_count(self, threshold: int = 5) -> int:
        """Cantidad de productos activos con stock por debajo del umbral."""
        stmt = select(func.count(Producto.id)).where(
            Producto.stock_cantidad <= threshold,
            Producto.deleted_at.is_(None),
        )
        return self.session.exec(stmt).one_or_none() or 0

    # ── Gráficos ──────────────────────────────────────────────────────────────

    def get_sales_over_time(self, start_date: datetime, end_date: datetime) -> list:
        """Ventas totales y cantidad de pedidos ENTREGADO agrupados por día."""
        stmt = (
            select(
                func.date(Pedido.created_at).label("fecha"),
                func.sum(Pedido.total).label("total"),
                func.count(Pedido.id).label("cantidad"),
            )
            .where(
                Pedido.estado_codigo == "ENTREGADO",
                Pedido.created_at >= start_date,
                Pedido.created_at <= end_date,
            )
            .group_by(func.date(Pedido.created_at))
            .order_by(func.date(Pedido.created_at))
        )
        return self.session.exec(stmt).all()

    def get_orders_by_status(self, start_date: datetime, end_date: datetime) -> list:
        """Cantidad de pedidos agrupados por estado en el rango de fechas."""
        stmt = (
            select(
                Pedido.estado_codigo,
                func.count(Pedido.id).label("cantidad"),
            )
            .where(
                Pedido.created_at >= start_date,
                Pedido.created_at <= end_date,
            )
            .group_by(Pedido.estado_codigo)
        )
        return self.session.exec(stmt).all()

    def get_top_products(self, start_date: datetime, end_date: datetime, limit: int = 5) -> list:
        """Productos más vendidos (por unidades) en pedidos ENTREGADO."""
        stmt = (
            select(
                Producto.name,
                func.sum(DetallePedido.cantidad).label("vendidos"),
            )
            .join(DetallePedido, DetallePedido.producto_id == Producto.id)
            .join(Pedido, Pedido.id == DetallePedido.pedido_id)
            .where(
                Pedido.estado_codigo == "ENTREGADO",
                Pedido.created_at >= start_date,
                Pedido.created_at <= end_date,
            )
            .group_by(Producto.name)
            .order_by(func.sum(DetallePedido.cantidad).desc())
            .limit(limit)
        )
        return self.session.exec(stmt).all()
