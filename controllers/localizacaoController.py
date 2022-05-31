from models.localizacao import Localizacao
from config.mongodb import colLocalizacao
from config.redisdb import r
import uuid
from schemas.localizacaoSchema import localizacaoEntity, localizacoesEntity



# cria a localização e retorna o id inserido
def create_localizacao_mongodb(newLocalizacao, newConcelho):
    try:
        localizacaoObject = Localizacao(localizacao=newLocalizacao, concelho=newConcelho)

        # upsert with replace_one
        created = colLocalizacao.replace_one(
            {"localizacao": localizacaoObject.localizacao,"concelho": localizacaoObject.concelho}, dict(localizacaoObject), upsert=True)

        if created.upserted_id is not None:
            localizacaoID = created.upserted_id
        else:
            localizacaoID = colLocalizacao.find_one({"concelho": localizacaoObject.concelho,"localizacao":localizacaoObject.localizacao})["_id"]

    except Exception as e:
        print(e)
        return None

    return localizacaoID


def create_localizacao_redis(newLocalizacao, newConcelho):
    try:
        valueID = uuid.uuid4().hex
        localizacao = {"localizacao": newLocalizacao, "concelho": newConcelho}
        keys = r.keys('*')
        if keys:
            for key in r.scan_iter():
                if r.hgetall(key) == localizacao:
                    r.hmset(key, localizacao)
                    print('Updated vendedor with id:', key)
                    return valueID
            r.hmset(valueID, localizacao)
            print('Vendedor inserted')
            return valueID
        else:
            r.hmset(valueID, localizacao)
            print('Vendedor inserted')
            return valueID
    except Exception as e:
        print(e)
        return None




