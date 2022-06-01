from models.vendedor import Vendedor
from config.mongodb import colVendedor
from config.redisdb import rvendedor
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
        alreadyExists = False

        vendedorCreated = {"name": newName}

        keys = rvendedor.keys('*')

        if keys:
            for key in keys:
                if rvendedor.hgetall(key) == vendedorCreated:
                    alreadyExists = True
                    valueID = key
                    break

        if not alreadyExists:
            rvendedor.hmset(valueID, vendedorCreated)

    except Exception as e:
        print(e)
        return None

    return valueID