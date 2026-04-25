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

    def get_by_id(self,id:int)-> Ingrediente:
        return self.session.get(Ingrediente,id)

    def get_by_name(self,name:str)-> Ingrediente:
        return self.session.exec(
            select(Ingrediente).where(Ingrediente.name == name)
        ).first()
    
    def add(self, producto):
        self.session.add(producto)
        self.session.flush()  
        return producto

    def get_all(self)->list[Ingrediente]:
     return self.session.exec(
         select(Ingrediente)
        ).all()

    def delete(self,ingrediente:Ingrediente)-> None:
     self.session.delete(ingrediente)