from fastapi import APIRouter, Depends
from sqlmodel import Session
from datetime import datetime, timedelta
from app.core.database import get_session
from app.core.deps import require_role
from app.modules.dashboard.service import DashboardService
from app.modules.dashboard.schema import DashboardKpis, ChartResponse

router = APIRouter(prefix="/dashboard", tags=["Dashboard"])

def get_dashboard_service(session: Session = Depends(get_session)) -> DashboardService:
    return DashboardService(session)

@router.get("/kpis", response_model=DashboardKpis)
def get_kpis(
    service: DashboardService = Depends(get_dashboard_service),
    _=Depends(require_role(["ADMIN"]))
):
    """
    Obtiene los KPIs principales (Recaudación, Pedidos completados, pendientes, bajo stock).
    """
    return service.get_kpis()

@router.get("/sales-over-time", response_model=ChartResponse)
def get_sales_over_time(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    service: DashboardService = Depends(get_dashboard_service),
    _=Depends(require_role(["ADMIN"]))
):
    """
    Obtiene las ventas agrupadas por día para un gráfico de líneas o barras.
    Por defecto, los últimos 30 días.
    """
    if not end_date:
        end_date = datetime.utcnow()
    if not start_date:
        start_date = end_date - timedelta(days=30)
        
    return service.get_sales_over_time(start_date, end_date)

@router.get("/orders-by-status", response_model=ChartResponse)
def get_orders_by_status(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    service: DashboardService = Depends(get_dashboard_service),
    _=Depends(require_role(["ADMIN"]))
):
    """
    Obtiene la cantidad de pedidos por cada estado para un gráfico de torta/donut.
    Por defecto, los últimos 30 días.
    """
    if not end_date:
        end_date = datetime.utcnow()
    if not start_date:
        start_date = end_date - timedelta(days=30)
        
    return service.get_orders_by_status(start_date, end_date)

@router.get("/top-products", response_model=ChartResponse)
def get_top_products(
    start_date: datetime | None = None,
    end_date: datetime | None = None,
    limit: int = 5,
    service: DashboardService = Depends(get_dashboard_service),
    _=Depends(require_role(["ADMIN"]))
):
    """
    Obtiene los productos más vendidos para un gráfico de barras horizontales o lista.
    Por defecto, los últimos 30 días.
    """
    if not end_date:
        end_date = datetime.utcnow()
    if not start_date:
        start_date = end_date - timedelta(days=30)
        
    return service.get_top_products(start_date, end_date, limit)
