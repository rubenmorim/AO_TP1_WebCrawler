from pydantic import BaseModel


class Localizacao(BaseModel):
    localizacao: str
    concelho: str



