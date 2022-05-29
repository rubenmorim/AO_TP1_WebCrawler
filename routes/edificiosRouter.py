from fastapi import APIRouter
from controllers.edificioController import find_all_edificios_mongodb, create_edificio_mongodb, create_edificio_redis, \
    find_all_edificios_redis

from models.edificio import Edificio

# Router variable
edificioRouter = APIRouter()


@edificioRouter.get("/api/edificios_mongo")
async def get_all_edificios_mongodb():
    return await find_all_edificios_mongodb()


@edificioRouter.get("/api/edificios_redis")
async def get_all_edificios_redis():
    return await find_all_edificios_redis()


@edificioRouter.post("/api/edificios_mongo")
async def post_edificio_mongodb(edificio:Edificio):
    return await create_edificio_mongodb(edificio)


@edificioRouter.post("/api/edificios_redis")
async def post_edificio_redis(edificio:Edificio):
    return await create_edificio_redis(edificio)



