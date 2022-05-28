from controllers.edificioController import create_edificio_mongodb
from config.mongodb import col
from models.edificio import Edificio


class PostsSpiderPipeline(object):

    def __init__(self):
        self.col = col

    def process_item(self, item, spider):
        try:
            self.col.insert_one(dict(item))
        except Exception as e:
            print(e)

        print("processing")
        return item