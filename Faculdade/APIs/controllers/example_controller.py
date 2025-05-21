from fastapi import APIRouter
from pydantic import BaseModel
from services.example_service import get_data, save_data , delete_data

router = APIRouter()

class ExampleRequest(BaseModel):
    name: str
    age: int

@router.get("/example")
async def get_example():
    return {
        "status": "success",
        "data": get_data()
    }

@router.post("/example")
async def post_example(data: ExampleRequest):
    processed = save_data(data.dict())
    return {
        "status": "success",
        "message": "Data received and processed",
        "processed": processed
    }
@router.delete("/example")
async def delete_example(data: ExampleRequest):
    deleted = delete_data(data.dict())
    return{
        "status": "success",
        "messege": "Data deleted",
        "deleted" : deleted
    }