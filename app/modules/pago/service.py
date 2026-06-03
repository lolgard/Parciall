from fastapi import HTTPException
from app.modules.pago.model import Pago
from app.modules.pago.schema import PagoCreate, PagoUpdate
from app.modules.pago.repository import PagoRepository
from app.modules.pedido.unit_of_work import PedidoUnitOfWork

class PagoService:
    def __init__(self, pago_repo: PagoRepository, uow: PedidoUnitOfWork):
        self.pago_repo = pago_repo
        self.uow = uow

    def get_by_pedido_id(self, pedido_id: int):
        return self.pago_repo.get_by_pedido_id(pedido_id)

    def create(self, data: PagoCreate):
        with self.uow as uow:
            pedido = uow.pedidos.get_by_id(data.pedido_id)
            if not pedido:
                raise HTTPException(status_code=404, detail="Pedido no encontrado")
            
            pago = Pago(**data.dict())
            return self.pago_repo.add(pago)

    def update(self, pago_id: int, data: PagoUpdate):
        with self.uow as uow:
            pago = self.pago_repo.get_by_id(pago_id)
            if not pago:
                raise HTTPException(status_code=404, detail="Pago no encontrado")
            
            for field, value in data.dict(exclude_unset=True).items():
                setattr(pago, field, value)
            
            return self.pago_repo.update(pago)
