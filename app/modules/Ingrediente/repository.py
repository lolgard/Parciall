from datetime import datetime

from app.core.repository import BaseRepository
from app.modules.Ingrediente.model import Ingrediente
from app.modules.Ingrediente.schema import IngredienteCreate
from sqlmodel import Session, select
class IngredienteRepository(BaseRepository):
    def __init__(self,session:Session):
        self.session = session 
        

    def create(self,data:IngredienteCreate)-> Ingrediente:
        ingrediente= Ingrediente(**data.dict())
        self.session.add(ingrediente)
        return ingrediente 

    def get_by_id(self, id: int, include_inactivos: bool = False) -> Ingrediente | None:        
        ingrediente = self.session.get(Ingrediente, id)
        
        if not ingrediente:
            return None
        if not include_inactivos and ingrediente.deleted_at is not None:
            return None
        return ingrediente

    def get_by_name(self,name:str)-> Ingrediente:
        return self.session.exec(
            select(Ingrediente).where(Ingrediente.name == name)
        ).first()
    
    def add(self, producto):
        self.session.add(producto)
        self.session.flush()  
        return producto

    def get_all(self, include_inactivos: bool = False) -> list[Ingrediente]:
        q = select(Ingrediente)
        if not include_inactivos:
            q = q.where(Ingrediente.deleted_at == None)
        return self.session.exec(q).all()

    def delete(self,ingrediente:Ingrediente)-> None:
     ingrediente.deleted_at = datetime.utcnow()
     self.session.add(ingrediente)
    