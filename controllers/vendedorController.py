from models.vendedor import Vendedor
from config.mongodb import colVendedor
from config.redisdb import r
import uuid
from schemas.vendedorSchema import vendedorEntity,vendedoresEntity



# cria o edificio e retorna o id inserido
def create_vendedor_mongodb(newName):
    try:
        vendedor = Vendedor(name=newName)

        # upsert with replace_one
        created = colVendedor.replace_one(
            {"name": vendedor.name}, dict(vendedor), upsert=True)
        if created.upserted_id is not None:
            vendedorID = created.upserted_id
        else:
            vendedorID = colVendedor.find_one({"name": newName})["_id"]

    except Exception as e:
        print(e)
        return None

    return vendedorID


def create_vendedor_redis(newName):
    try:
        valueID = uuid.uuid4().hex
        vendedor = {"name": newName}
        for key in r.scan_iter():
            if r.hgetall(key) == vendedor:
                r.hmset(key, vendedor)
                print('Updated vendedor with id:', key)
            else:
                r.hmset(valueID, vendedor)
                print('Vendedor inserted')

    except Exception as e:
        print(e)
        return None

    return valueID