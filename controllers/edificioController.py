from models.edificio import Edificio
from config.mongodb import colEdificio
from config.redisdb import r
from schemas.edificioSchema import edificioEntity, edificiosEntity


async def find_all_edificios_mongodb():
    return edificiosEntity(colEdificio.find())


async def find_all_edificios_redis():
    edificios = []
    for key in r.keys():
        edificios.append(r.hgetall(key))
    return edificios


# cria o edificio e retorna o id inserido
def create_edificio_mongodb(newName, newType, newPrice):
    try:
        edificio = Edificio(name=newName, type=newType, price=newPrice)
        # upsert with replace_one
        created = colEdificio.replace_one(
            {"name": edificio.name, "type": edificio.type, "price": edificio.price}, dict(edificio), upsert=True)
        # verificar o upsert
        if created.matched_count == 1:
            print("Edificio already Inserted")
        else:
            print('Upserted edificio with id:', created.upserted_id)
    except Exception as e:
        return "Ocorreu algum erro ao inserir Edificio"
    return "Edificio Upserted"


def create_edificio_redis(newName, newType, newPrice):
    try:
        valueID = newName + "-" + newType + "-" + newPrice
        edificio = {"name": newName, "type": newType, "price": newPrice}
        a = r.hkeys(valueID)
        if (len(a) > 0):
            r.hmset(valueID, edificio)
            print('Updated edificio with id:', valueID)
        else:
            r.hmset(valueID, edificio)
            print('Edificio inserted')
    except Exception as e:
        return "Ocorreu algum erro ao inserir Edificio"
    return "Edificio Upserted"
