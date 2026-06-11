"""
DashboardUnitOfWork
===================
UoW para el módulo Dashboard. Solo lectura — no realiza escrituras,
pero encapsula la sesión con el mismo contrato de contexto que el resto
de los módulos (BaseUnitOfWork), garantizando manejo consistente de
sesiones y transacciones.
"""
from sqlmodel import Session
from app.core.unit_of_work import BaseUnitOfWork
from app.modules.dashboard.repository import DashboardRepository


class DashboardUnitOfWork(BaseUnitOfWork):

    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.dashboard = DashboardRepository(session)
