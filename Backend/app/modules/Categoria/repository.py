from app.core.repository import BaseRepository
from app.modules.Categoria.model import Categoria
from app.modules.Categoria.schema import CategoriaCreate
from sqlmodel import Session, select
class CategoriaRepository(BaseRepository):
    def __init__(self,session:Session):
        self.session = session 
        

    def create(self,data:CategoriaCreate)-> Categoria:
        categoria= Categoria(**data.dict())
        self.session.add(categoria)
        return categoria 
    
    def get_by_id(self,id:int)-> Categoria:
        return self.session.get(Categoria,id)

    def get_by_name(self,nombre:str)-> Categoria:
        return self.session.exec(
            select(Categoria).where(Categoria.nombre == nombre)
        ).first()
    
    def update(self, categoria: Categoria) -> Categoria:
        self.session.add(categoria)
        self.session.flush()
        return categoria
    
    def add(self, categoria: Categoria) -> Categoria:
        self.session.add(categoria)
        self.session.flush()
        return categoria

    def get_all(self)->list[Categoria]:
     return self.session.exec(
         select(Categoria)
        ).all()

    def delete(self,categoria:Categoria)-> None:
     self.session.delete(categoria)