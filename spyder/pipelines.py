from controllers.edificioController import create_edificio_mongodb
from config.mongodb import col
from models.edificio import Edificio


class PostsSpiderPipeline(object):

    def __init__(self):
        self.col = col

    def process_item(self, item, spider):
        aaa = Edificio(name="eeh", type="teste", price=24)
        try:
            self.col.insert_one(dict(aaa))
        except Exception as e:
            print(e)

        return item