from controllers.edificioController import create_edificio_mongodb
from config.mongodb import colEdificio
from controllers.edificioController import create_edificio_mongodb
from controllers.vendedorController import create_vendedor_mongodb
from controllers.localizacaoController import create_localizacao_mongodb
from controllers.edificioController import create_edificio_redis
from controllers.vendedorController import create_vendedor_redis
from controllers.localizacaoController import create_localizacao_redis

class PostsSpiderPipeline(object):

    def __init__(self):
        self.col = colEdificio

    def process_item(self, item, spider):
        try:

            resultLocalizcaoMongoDB = create_localizacao_mongodb(item["concelho"], item["localizacao"])
            resultVendedorMongoDB = create_vendedor_mongodb(item["nameVendedor"])
            create_edificio_mongodb(item["name"], item["type"], item["price"], str(resultVendedorMongoDB), str(resultLocalizcaoMongoDB))

            resultLocalizcaoRedis = create_localizacao_redis(item["concelho"],item["localizacao"])
            resultVendedorRedis = create_vendedor_redis(item["nameVendedor"])
            create_edificio_redis(item["name"], item["type"], item["price"], str(resultVendedorRedis), str(resultLocalizcaoRedis))
        except Exception as e:
            print(e)
            print("falha ao inserir")

        return item