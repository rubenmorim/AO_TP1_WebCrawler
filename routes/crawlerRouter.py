from fastapi import APIRouter,Request
from spyder.zomeSpyder import PostsSpider
from scrapyscript import Job, Processor
from models.CrawlerSettings import CrawlerSettings

# Router variable
crawlerRouter = APIRouter()



# importar dados e correr crawler
@crawlerRouter.post("/api/importar")
async def import_edificios(crawlerSettings: CrawlerSettings):
    post_settings = dict(crawlerSettings)

    # para poder correr multiplos spiders, sem bloquear o twisted.reactor
    job = Job(PostsSpider,  start_id=post_settings["start_id"], num_pages=post_settings["num_pages"])
    processor = Processor(settings=None)
    processor.run(job)


    return "Importação concluida"