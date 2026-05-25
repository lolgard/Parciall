from sqlmodel import SQLModel


class RolBase(SQLModel):
    code : str
    name  : str
    descripcion : str

class RolCreate(RolBase):
    pass

class RolRead(RolBase):
    pass
 
class RolUpdate(SQLModel):
    code : str | None = None
    name  : str | None = None
    descripcion : str | None = None
    

