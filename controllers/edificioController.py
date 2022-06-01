from models.edificio import Edificio
from config.mongodb import colEdificio
from config.redisdb import redificio
import uuid
from schemas.edificioSchema import edificioEntity, edificiosEntity


async def find_all_edificios_mongodb():
    return edificiosEntity(colEdificio.find())


async def find_all_edificios_redis():
    edificios = []
    for key in redificio.keys():
        edificios.append(redificio.hgetall(key))
    return edificios


# cria o edificio e retorna o id inserido
def create_edificio_mongodb(newName, newType, newPrice,vendedorID,localizacaoID):
    try:
        edificio = Edificio(name=newName, type=newType, price=newPrice,vendedorID=vendedorID,localizacaoID=localizacaoID)
        # upsert with replace_one
        created = colEdificio.replace_one(
            {"name": edificio.name, "type": edificio.type, "price": edificio.price, "vendedorID" : vendedorID,"localizacaoID":localizacaoID}, dict(edificio), upsert=True)
        # verificar o upsert
        if created.matched_count == 1:
            print("MongoDB - Edificio already Inserted")
        else:
            print('MongoDB - Upserted edificio with id:', created.upserted_id)
    except Exception as e:
        print(e)
        return "Ocorreu algum erro ao inserir Edificio"

    return "Edificio Upserted"


def create_edificio_redis(newName, newType, newPrice, vendedorID, localizacaoID):
    try:
        valueID = uuid.uuid4().hex
        alreadyExists = False

        newNameParsed = newName.replace(u' \xa0', u' ')
        edificioCreated = {"name": newNameParsed, "type": newType, "price": str(newPrice), "vendedorID": vendedorID, "localizacaoID": localizacaoID}

        keys = redificio.keys('*')
        if keys:
            for key in keys:
                if redificio.hgetall(key) == edificioCreated:
                    alreadyExists = True
                    valueID = key
                    break

        if not alreadyExists:
            redificio.hmset(valueID, edificioCreated)
            print("Inseriu edificio redis")

    except Exception as e:
        print(e)
        return None

    return valueID