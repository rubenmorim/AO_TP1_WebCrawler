from models.localizacao import Localizacao
from config.mongodb import colLocalizacao
from config.redisdb import rlocalizacao
import uuid
from schemas.localizacaoSchema import localizacaoEntity, localizacoesEntity


# cria a localização e retorna o id inserido
def create_localizacao_mongodb(newLocalizacao, newConcelho):
    try:
        localizacaoObject = Localizacao(localizacao=newLocalizacao, concelho=newConcelho)

        # upsert with replace_one
        created = colLocalizacao.replace_one(
            {"localizacao": localizacaoObject.localizacao, "concelho": localizacaoObject.concelho},
            dict(localizacaoObject), upsert=True)

        if created.upserted_id is not None:
            localizacaoID = created.upserted_id
        else:
            localizacaoID = colLocalizacao.find_one(
                {"concelho": localizacaoObject.concelho, "localizacao": localizacaoObject.localizacao})["_id"]

    except Exception as e:
        print(e)
        return None

    return localizacaoID


def create_localizacao_redis(newLocalizacao, newConcelho):
    try:
        valueID = uuid.uuid4().hex
        alreadyExists = False

        newConcelhoParsed = newConcelho.replace(u'\xa0', u' ')
        localizacaoCreated = {"localizacao": newLocalizacao, "concelho": newConcelhoParsed}

        keys = rlocalizacao.keys('*')

        if keys:
            for key in keys:
                if rlocalizacao.hgetall(key) == localizacaoCreated:
                    alreadyExists = True
                    valueID = key
                    break

        if not alreadyExists:
            rlocalizacao.hmset(valueID, localizacaoCreated)

    except Exception as e:
        print(e)
        return None

    return valueID
