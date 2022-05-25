from fastapi import APIRouter
from controllers.edificioController import find_all_edificios_mongodb, create_edificio_mongodb

from models.edificio import Edificio

# Router variable
edificioRouter = APIRouter()


@edificioRouter.get("/api/edificios")
async def get_all_edificios_mongodb():
    return await find_all_edificios_mongodb()

@edificioRouter.post("/api/edificios")
async def post_edificio_mongodb(edificio:Edificio):
    return await create_edificio_mongodb(edificio)



