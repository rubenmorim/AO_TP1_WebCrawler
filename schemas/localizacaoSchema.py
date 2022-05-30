# dicionário edificio
from typing import List
def localizacaoEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "localizacao": str(item["localizacao"]),
        "concelho": str(item["concelho"])
    }


def localizacoesEntity(list) -> list:
    return [localizacaoEntity(item) for item in list]