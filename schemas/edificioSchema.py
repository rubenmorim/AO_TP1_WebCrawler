# dicionário edificio
from typing import List


def edificioEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": str(item["name"]),
        "type": str(item["type"]),
        "price": int(item["price"]),
        "vendedorID": str(item["vendedorID"]),
        "localizacaoID": str(item["localizacaoID"])
    }


def edificiosEntity(list) -> list:
    return [edificioEntity(item) for item in list]
