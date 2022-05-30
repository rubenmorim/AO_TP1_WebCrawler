from controllers.edificioController import create_edificio_mongodb
from config.mongodb import colEdificio
from controllers.edificioController import create_edificio_mongodb
from controllers.vendedorController import create_vendedor_mongodb

class PostsSpiderPipeline(object):

    def __init__(self):
        self.col = colEdificio

    def process_item(self, item, spider):
        try:
            result = create_vendedor_mongodb(item["nameVendedor"])
            create_edificio_mongodb(item["name"],item["type"],item["price"],str(result))
        except Exception as e:
            print(e)
            print("falha ao inserir")

        return item