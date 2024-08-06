from fastapi import APIRouter

hello_router = APIRouter()

@hello_router.get("/hello")
async def hello_world():
    return {"message": "hello world"}