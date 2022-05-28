import scrapy
from spyder.pipelines import PostsSpiderPipeline
from utils.utils import parse_preco


class PostsSpider(scrapy.Spider):
    name = "posts"

    custom_settings = {
        'DOWNLOAD_DELAY': 3,
        'DEPTH_LIMIT': 3,
        'LOG_ENABLED': False,
        'COOKIES_ENABLED': False,
        'CONCURRENT_ITEMS': 1,
        "ITEM_PIPELINES" : {
        PostsSpiderPipeline: 300,
        }
    }


    def __init__(self, start_id=1, num_pages=1, *args, **kwargs):
        super(PostsSpider, self).__init__(*args, **kwargs)

        self.start_urls = list(
            map(lambda x: f'https://www.zome.pt/pt/imoveis/venda/page-{x}', range(start_id, start_id + num_pages)))

    def parse(self, response):
        print(f"--- a processar o Zome em {response.url} ---")
        for post in response.css('.mode-view-grid .modulo .modulo_in .z_mod_grupo'):
            price = post.css('.mod_fim .mod_fim_in .mod_fim_valor::text').get()
            priceParsed = parse_preco(price)
            yield{
                "price":priceParsed,
                "name": post.css('.mod_info .mod_info_in .mod_info_loc .mod_info_lc_in .mod_tipo .z_modt_tipo::text').get(),
                "type": post.css('.mod_info .mod_info_in .mod_info_loc .mod_info_lc_in .mod_tipo .z_modt_tipo em::text').get()
            }



        # faz um for a todos e adiciona ao asyncio.gather, só quando todos terminarem é que continua
        # # asyncio.gather(*[insertDocument(post) for post in response.css('.mode-view-grid .modulo .modulo_in .z_mod_grupo')])
        # for post in response.css('.mode-view-grid .modulo .modulo_in .z_mod_grupo'):
        #     insertDocument(post)
        # loop = asyncio.get_event_loop()
        # loop.run_until_complete(createPromiseAll(response))
        # loop.close()
