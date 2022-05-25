from fastapi import FastAPI
from routes.edificiosRouter import edificioRouter
from routes.crawlerRouter import crawlerRouter

app = FastAPI()

# routes
app.include_router(edificioRouter)
app.include_router(crawlerRouter)


