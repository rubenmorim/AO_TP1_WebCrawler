from pydantic import BaseModel


class Edificio(BaseModel):
    name:str
    type:str
    price:int
    vendedorID:str
    localizacaoID:str


