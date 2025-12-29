from fastapi import APIRouter

# THIS MUST BE NAMED base_router
base_router = APIRouter()

@base_router.get("/")
async def welcome():
    return {"message": "Welcome to mini-RAG!"}