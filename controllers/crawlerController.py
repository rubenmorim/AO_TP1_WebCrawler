from utils.utils import parse_preco
from controllers.edificioController import create_edificio_mongodb
import asyncio
import threading



async def insertDocument(post):
    print("teste")
    name = post.css('.mod_info .mod_info_in .mod_info_loc .mod_info_lc_in .mod_tipo .z_modt_tipo::text').get()
    type = post.css(
        '.mod_info .mod_info_in .mod_info_loc .mod_info_lc_in .mod_tipo .z_modt_tipo em::text').get()
    preco = post.css('.mod_fim .mod_fim_in .mod_fim_valor::text').get()
    precoParsed = parse_preco(preco)


    await create_edificio_mongodb(name, type, precoParsed)


    # processar o post e inserir o necessário , aqui embaixo pode ser adicionado também outras bases de dados

