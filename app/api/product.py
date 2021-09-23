from fastapi import APIRouter
from app.api import schema

# instance router ขึ้นมา
router = APIRouter()

@router.get("/")
def get_product():
  return[1,2,3]

@router.get("/{id}")
def get_product_by_id(id:str):
  return {"id":id}

