from sqlmodel import Session, select, func
from datetime import datetime, timedelta, time
from sqlalchemy.orm import aliased
from app.modules.pedido.model import Pedido
from app.modules.detallePedido.model import DetallePedido
from app.modules.Producto.model import Producto
from app.modules.dashboard.schema import DashboardKpis, KpiMetric, ChartDataPoint, ChartResponse

class DashboardService:
    def __init__(self, session: Session):
        self.session = session

    def _calculate_trend(self, current: float, previous: float) -> tuple[str, str]:
        if previous == 0:
            if current > 0:
                return "+100%", "up"
            return "0%", "neutral"
        
        diff = current - previous
        percentage = (diff / previous) * 100
        
        status = "neutral"
        if percentage > 0:
            status = "up"
            trend_str = f"+{percentage:.0f}%"
        elif percentage < 0:
            status = "down"
            trend_str = f"{percentage:.0f}%"
        else:
            trend_str = "0%"
            
        return trend_str, status

    def get_kpis(self) -> DashboardKpis:
        today_start = datetime.combine(datetime.utcnow().date(), time.min)
        yesterday_start = today_start - timedelta(days=1)
        
        # 1. Recaudación Hoy vs Ayer (Solo ENTREGADO)
        def get_revenue(start_dt, end_dt):
            stmt = select(func.sum(Pedido.total)).where(
                Pedido.estado_codigo == "ENTREGADO",
                Pedido.created_at >= start_dt,
                Pedido.created_at < end_dt
            )
            return self.session.exec(stmt).one_or_none() or 0.0

        rev_today = get_revenue(today_start, datetime.utcnow())
        rev_yesterday = get_revenue(yesterday_start, today_start)
        
        rev_trend, rev_status = self._calculate_trend(rev_today, rev_yesterday)
        
        recaudacion = KpiMetric(
            value=rev_today,
            trend=f"{rev_trend} vs ayer",
            status=rev_status,
            label="Recaudación Hoy",
            subtext="En base a pedidos entregados"
        )
        
        # 2. Pedidos Completados Hoy vs Ayer
        def get_completed_orders(start_dt, end_dt):
            stmt = select(func.count(Pedido.id)).where(
                Pedido.estado_codigo == "ENTREGADO",
                Pedido.created_at >= start_dt,
                Pedido.created_at < end_dt
            )
            return self.session.exec(stmt).one_or_none() or 0

        comp_today = get_completed_orders(today_start, datetime.utcnow())
        comp_yesterday = get_completed_orders(yesterday_start, today_start)
        
        comp_trend, comp_status = self._calculate_trend(comp_today, comp_yesterday)
        
        pedidos_completados = KpiMetric(
            value=comp_today,
            trend=f"{comp_trend} vs ayer",
            status=comp_status,
            label="Pedidos Completados",
            subtext="Pedidos en estado ENTREGADO"
        )
        
        # 3. Pedidos Pendientes Hoy vs Ayer
        # Pendientes incluyen PENDIENTE y EN_PREP
        pendientes_estados = ["PENDIENTE", "CONFIRMADO", "EN_PREP", "LISTO"]
        
        def get_pending_orders(start_dt, end_dt):
            stmt = select(func.count(Pedido.id)).where(
                Pedido.estado_codigo.in_(pendientes_estados),
                Pedido.created_at >= start_dt,
                Pedido.created_at < end_dt
            )
            return self.session.exec(stmt).one_or_none() or 0
            
        pend_today = get_pending_orders(today_start, datetime.utcnow())
        pend_yesterday = get_pending_orders(yesterday_start, today_start)
        
        # Para pendientes, menos es mejor, así que invertimos el status visual (opcional)
        pend_trend, pend_status_raw = self._calculate_trend(pend_today, pend_yesterday)
        # Si suben los pendientes, es "down" (malo), si bajan es "up" (bueno)
        pend_status = "down" if pend_status_raw == "up" else ("up" if pend_status_raw == "down" else "neutral")
        
        pedidos_pendientes = KpiMetric(
            value=pend_today,
            trend=f"{pend_trend} vs ayer",
            status=pend_status,
            label="Pedidos Pendientes",
            subtext="Pedidos no finalizados"
        )
        
        # 4. Productos Bajo Stock
        # Contamos cuántos productos tienen stock_cantidad <= 5
        stmt_stock = select(func.count(Producto.id)).where(
            Producto.stock_cantidad <= 5,
            Producto.deleted_at.is_(None)
        )
        low_stock_count = self.session.exec(stmt_stock).one_or_none() or 0
        
        bajo_stock = KpiMetric(
            value=low_stock_count,
            trend="Revisar inventario",
            status="down" if low_stock_count > 0 else "up",
            label="Productos Bajo Stock",
            subtext="Artículos con 5 unidades o menos"
        )
        
        return DashboardKpis(
            recaudacion=recaudacion,
            pedidos_completados=pedidos_completados,
            pedidos_pendientes=pedidos_pendientes,
            bajo_stock=bajo_stock
        )
        
    def get_sales_over_time(self, start_date: datetime, end_date: datetime) -> ChartResponse:
        # Esto depende de tu dialecto SQL para truncar fechas, en Postgres es date_trunc
        # En SQLite puro es más complejo, pero SQLModel/SQLAlchemy puede agrupar por func.date
        
        stmt = select(
            func.date(Pedido.created_at).label("fecha"),
            func.sum(Pedido.total).label("total")
        ).where(
            Pedido.estado_codigo == "ENTREGADO",
            Pedido.created_at >= start_date,
            Pedido.created_at <= end_date
        ).group_by(func.date(Pedido.created_at)).order_by(func.date(Pedido.created_at))
        
        results = self.session.exec(stmt).all()
        
        data = []
        for row in results:
            data.append(ChartDataPoint(label=str(row.fecha), value=float(row.total or 0)))
            
        return ChartResponse(data=data)

    def get_orders_by_status(self, start_date: datetime, end_date: datetime) -> ChartResponse:
        stmt = select(
            Pedido.estado_codigo,
            func.count(Pedido.id).label("cantidad")
        ).where(
            Pedido.created_at >= start_date,
            Pedido.created_at <= end_date
        ).group_by(Pedido.estado_codigo)
        
        results = self.session.exec(stmt).all()
        
        data = []
        for row in results:
            data.append(ChartDataPoint(label=str(row.estado_codigo), value=int(row.cantidad or 0)))
            
        return ChartResponse(data=data)

    def get_top_products(self, start_date: datetime, end_date: datetime, limit: int = 5) -> ChartResponse:
        # Sumamos las cantidades de DetallePedido agrupando por Producto
        stmt = select(
            Producto.name,
            func.sum(DetallePedido.cantidad).label("vendidos")
        ).join(
            DetallePedido, DetallePedido.producto_id == Producto.id
        ).join(
            Pedido, Pedido.id == DetallePedido.pedido_id
        ).where(
            Pedido.estado_codigo == "ENTREGADO",
            Pedido.created_at >= start_date,
            Pedido.created_at <= end_date
        ).group_by(Producto.name).order_by(func.sum(DetallePedido.cantidad).desc()).limit(limit)
        
        results = self.session.exec(stmt).all()
        
        data = []
        for row in results:
            data.append(ChartDataPoint(label=str(row.name), value=int(row.vendidos or 0)))
            
        return ChartResponse(data=data)
