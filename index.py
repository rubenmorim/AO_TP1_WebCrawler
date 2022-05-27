from fastapi import FastAPI
from routes.edificiosRouter import edificioRouter
from routes.crawlerRouter import crawlerRouter
import uvicorn

app = FastAPI()

# routes
app.include_router(edificioRouter)
app.include_router(crawlerRouter)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8001)
