
from datetime import datetime

from sqlmodel import Session, select

from app.core.repository import BaseRepository
from app.modules.direccionEntrega.model import DireccionEntrega


class DireccionEntregaRepository(BaseRepository):
    def __init__(self, session:Session):
        self.session=session

    def create(self, data):

        direccionEntrega = DireccionEntrega(**data.dict())
        direccionEntrega = self.session.add(direccionEntrega)

        return direccionEntrega
    
    def get_by_name(self,name:str)-> DireccionEntrega:
        return self. session.exec(
            select(DireccionEntrega).where(DireccionEntrega.bane == name)
        ).first()
    
    def get_by_id(self, id:int) -> DireccionEntrega | None:
        direccionEntrega = self.session.get(DireccionEntrega, id)

        if not direccionEntrega or direccionEntrega.deleted_at is not None:
            return None
        return direccionEntrega
    
    def get_all(self) -> list[DireccionEntrega]:
        DireccionEntregas =self.session.exec(
            select(DireccionEntrega).where(DireccionEntrega.deleted_at == None)
        ).all()
        for direccionEntrega in DireccionEntregas:
            self.session.refresh(direccionEntrega)
        return DireccionEntregas
    
    def update(self,direccionEntrega:DireccionEntrega) ->DireccionEntrega:
        self.session.add(direccionEntrega)
        self.session.flush()
        self.session.refresh(direccionEntrega)
        return direccionEntrega
    
    def delete(self,direccionEntrega:DireccionEntrega)-> None:
      

        direccionEntrega.deleted_at = datetime.utcnow()
        self.session.add(direccionEntrega)
        self.session.flush()