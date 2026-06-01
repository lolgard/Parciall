from sqlmodel import Session

from app.core.unit_of_work import BaseUnitOfWork
from app.modules.pedido.repository import PedidoRepository
from app.modules.detallePedido.repository import DetallePedidoRepository
from app.modules.historialEstadoPedido.repository import HistorialEstadoPedidoRepository
from app.modules.direccionEntrega.repository import DireccionEntregaRepository
from app.modules.formaPago.repository import FormaPagoRepository
from app.modules.Producto.repository import ProductoRepository

class PedidoUnitOfWork(BaseUnitOfWork):
    def __init__(self, session: Session) -> None:
        super().__init__(session)
        self.pedidos = PedidoRepository(session)
        self.detalles = DetallePedidoRepository(session)
        self.historial = HistorialEstadoPedidoRepository(session)
        self.direccion_entregas = DireccionEntregaRepository(session)
        self.formas_pago = FormaPagoRepository(session)
        self.productos = ProductoRepository(session)
