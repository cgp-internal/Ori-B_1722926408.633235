from fastapi import FastAPI

app = FastAPI()

from routes.hello import hello_router

app.include_router(hello_router)