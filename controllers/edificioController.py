from models.edificio import Edificio
from config.mongodb import conn
from schemas.edificioSchema import edificioEntity, edificiosEntity



async def find_all_edificios_mongodb():
    return edificiosEntity(conn.local.edificio.find())


# cria o edificio e retorna o id inserido
def create_edificio_mongodb(newName, newType, newPrice):
    try:
        edificio = Edificio(name="eeh", type="teste", price=24)
        # upsert with replace_one
        created = conn.local.edificio.replace_one(
            {"name": edificio.name, "type": edificio.type, "price": edificio.price}, dict(edificio), upsert=True)
        # verificar o upsert
        if created.matched_count == 1:
            print("Edificio already Inserted")
        else:
            print('Upserted edificio with id:', created.upserted_id)
    except Exception as e:
        return "Ocorreu algum erro ao inserir Edificio"
    return "Edificio Upserted"
