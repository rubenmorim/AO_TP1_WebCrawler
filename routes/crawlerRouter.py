from scrapy.crawler import CrawlerProcess
from fastapi import APIRouter
import sys


from zomeSpyder import PostsSpider

# Router variable
crawlerRouter = APIRouter()


# importar dados e correr crawler
@crawlerRouter.get("/api/importar")
async def import_edificios():
    try:
        process = CrawlerProcess()
        process.crawl(PostsSpider, start_id=14, num_pages=1)
        # delete reactor instance to let scrap again (bug)
        if "twisted.internet.reactor" in sys.modules:
            del sys.modules["twisted.internet.reactor"]
        process.start()
    except Exception as e:
        print(e)
        return "Ocorreu algum erro"
    print("Importação Concluida")
    return "Importação concluida"


