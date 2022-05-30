# dicionário edificio
from typing import List
def vendedorEntity(item) -> dict:
    return{
        "id":str(item["_id"]),
        "name": str(item["name"])
    }


def vendedoresEntity(list) -> list:
    return [vendedorEntity(item) for item in list]