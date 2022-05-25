import asyncio
import scrapy
from controllers.crawlerController import insertDocument



class PostsSpider(scrapy.Spider):
    name = "posts"

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'DEPTH_LIMIT': 3,
        'LOG_ENABLED': False,
        'COOKIES_ENABLED': False,
        'CONCURRENT_ITEMS': 1
    }

    def __init__(self, start_id=0, num_pages=100, *args, **kwargs):
        super(PostsSpider, self).__init__(*args, **kwargs)
        self.start_urls = list(
            map(lambda x: f'https://www.zome.pt/pt/imoveis/venda/page-{x}', range(start_id, start_id + num_pages)))



    async def parse(self, response):
        print(f"--- a processar o Zome em {response.url} ---")
        # uso de assincronismo no for... espera pela inserção do insertDocument que é uma função assincrona
        for f in asyncio.as_completed([insertDocument(post) for post in response.css('.mode-view-grid .modulo .modulo_in .z_mod_grupo')]):
            await f
