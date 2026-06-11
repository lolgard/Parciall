"""
DashboardService
================
Servicio de lógica de negocio para el Dashboard.

Utiliza DashboardUnitOfWork para el acceso a datos, siguiendo el
mismo contrato que el resto de los módulos del proyecto.
"""
from datetime import datetime, timedelta, time

from app.modules.dashboard.unit_of_work import DashboardUnitOfWork
from app.modules.dashboard.schema import (
    DashboardKpis,
    KpiMetric,
    ChartDataPoint,
    ChartResponse,
)


class DashboardService:

    def __init__(self, uow: DashboardUnitOfWork):
        self.uow = uow

    # ── Helpers ───────────────────────────────────────────────────────────────

    def _calculate_trend(self, current: float, previous: float) -> tuple[str, str]:
        """Calcula la variación porcentual y el estado (up/down/neutral)."""
        if previous == 0:
            return ("+100%", "up") if current > 0 else ("0%", "neutral")

        diff = current - previous
        percentage = (diff / previous) * 100

        if percentage > 0:
            return f"+{percentage:.0f}%", "up"
        elif percentage < 0:
            return f"{percentage:.0f}%", "down"
        return "0%", "neutral"

    # ── KPIs ──────────────────────────────────────────────────────────────────

    def get_kpis(self, start_date: datetime | None = None, end_date: datetime | None = None) -> DashboardKpis:
        now = datetime.utcnow()
        if not end_date:
            end_date = now
        
        if not start_date:
            # Por defecto: "Hoy" (desde la medianoche hasta ahora)
            current_start = datetime.combine(end_date.date(), time.min)
            delta = timedelta(days=1)
            previous_start = current_start - delta
            previous_end = current_start
            trend_label = "vs ayer"
        else:
            current_start = start_date
            delta = end_date - start_date
            # El período anterior tiene exactamente la misma duración y termina justo donde empieza el actual
            previous_start = current_start - delta
            previous_end = current_start
            
            # Si el filtro es exactamente de 1 día (ej. "Hoy"), mantenemos "vs ayer". Si no, "vs período anterior"
            if delta.days <= 1:
                trend_label = "vs ayer"
            else:
                trend_label = "vs período anterior"

        with self.uow as uow:
            # 1. Recaudación
            rev_current = uow.dashboard.get_revenue(current_start, end_date)
            rev_previous = uow.dashboard.get_revenue(previous_start, previous_end)
            rev_trend, rev_status = self._calculate_trend(rev_current, rev_previous)

            recaudacion = KpiMetric(
                value=rev_current,
                trend=f"{rev_trend} {trend_label}",
                status=rev_status,
                label="Recaudación",
                subtext="En base a pedidos entregados",
            )

            # 2. Pedidos completados
            comp_current = uow.dashboard.get_completed_orders_count(current_start, end_date)
            comp_previous = uow.dashboard.get_completed_orders_count(previous_start, previous_end)
            comp_trend, comp_status = self._calculate_trend(comp_current, comp_previous)

            pedidos_completados = KpiMetric(
                value=comp_current,
                trend=f"{comp_trend} {trend_label}",
                status=comp_status,
                label="Pedidos Completados",
                subtext="Pedidos en estado ENTREGADO",
            )

            # 3. Pedidos pendientes
            pend_current = uow.dashboard.get_pending_orders_count(current_start, end_date)
            pend_previous = uow.dashboard.get_pending_orders_count(previous_start, previous_end)
            pend_trend, pend_status_raw = self._calculate_trend(pend_current, pend_previous)
            # Invertimos el sentido: más pendientes es "peor" (down)
            pend_status = (
                "down" if pend_status_raw == "up"
                else "up" if pend_status_raw == "down"
                else "neutral"
            )

            pedidos_pendientes = KpiMetric(
                value=pend_current,
                trend=f"{pend_trend} {trend_label}",
                status=pend_status,
                label="Pedidos Pendientes",
                subtext="Pedidos no finalizados",
            )

            # 4. Productos con bajo stock (ignora fechas)
            low_stock_count = uow.dashboard.get_low_stock_count(threshold=5)

            bajo_stock = KpiMetric(
                value=low_stock_count,
                trend="Revisar inventario",
                status="down" if low_stock_count > 0 else "up",
                label="Productos Bajo Stock",
                subtext="Artículos con 5 unidades o menos",
            )

        return DashboardKpis(
            recaudacion=recaudacion,
            pedidos_completados=pedidos_completados,
            pedidos_pendientes=pedidos_pendientes,
            bajo_stock=bajo_stock,
        )

    # ── Gráficos ──────────────────────────────────────────────────────────────

    def get_sales_over_time(self, start_date: datetime, end_date: datetime) -> ChartResponse:
        with self.uow as uow:
            rows = uow.dashboard.get_sales_over_time(start_date, end_date)

        return ChartResponse(
            data=[
                ChartDataPoint(
                    label=str(row.fecha),
                    value=float(row.total or 0),
                    count=int(row.cantidad or 0),
                )
                for row in rows
            ]
        )

    def get_orders_by_status(self, start_date: datetime, end_date: datetime) -> ChartResponse:
        with self.uow as uow:
            rows = uow.dashboard.get_orders_by_status(start_date, end_date)

        return ChartResponse(
            data=[
                ChartDataPoint(label=str(row.estado_codigo), value=int(row.cantidad or 0))
                for row in rows
            ]
        )

    def get_top_products(self, start_date: datetime, end_date: datetime, limit: int = 5) -> ChartResponse:
        with self.uow as uow:
            rows = uow.dashboard.get_top_products(start_date, end_date, limit)

        return ChartResponse(
            data=[
                ChartDataPoint(label=str(row.name), value=int(row.vendidos or 0))
                for row in rows
            ]
        )
