from fastapi import APIRouter

# This name MUST match what main.py is looking for
base_router = APIRouter() 

@base_router.get("/")
async def welcome():
    return {"message": "Welcome to mini-RAG!"}