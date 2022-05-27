from fastapi import APIRouter,Request
from spyder.zomeSpyder import PostsSpider
from scrapyscript import Job, Processor


# Router variable
crawlerRouter = APIRouter()

# importar dados e correr crawler
@crawlerRouter.get("/api/importar")
async def import_edificios(request:Request):

    # para poder correr multiplos spiders, sem bloquear o twisted.reactor
    job = Job(PostsSpider,  start_id=1, num_pages=3)
    processor = Processor(settings=None)
    processor.run(job)

    return "Importação concluida"
