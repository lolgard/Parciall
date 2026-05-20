class UnidadDeMedidaBase(SQLModel):
    name: str
    symbol: str
    type: str

class UnidadDeMedidaCreate(UnidadDeMedidaBase):
    pass

class UnidadDeMedidaRead(UnidadDeMedidaBase):
    id : int

class 