from pydantic import BaseModel
from typing import List, Optional

class KpiMetric(BaseModel):
    value: float | int
    trend: str
    status: str # "up", "down", "neutral"
    label: str
    subtext: str

class DashboardKpis(BaseModel):
    recaudacion: KpiMetric
    pedidos_completados: KpiMetric
    pedidos_pendientes: KpiMetric
    bajo_stock: KpiMetric

class ChartDataPoint(BaseModel):
    label: str
    value: float | int

class ChartResponse(BaseModel):
    data: List[ChartDataPoint]
