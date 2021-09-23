from fastapi import APIRouter
from app.api import authen, product, transaction
from app.models import database

database.Base.metadata.create_all(database.engine, checkfirst=True) # สร้าง DB


api_router = APIRouter()

api_router.include_router(
  authen.router, 
  tags=["authen"]
) # tags เป็นเหมือนหมายเหตุ
api_router.include_router(
  product.router, 
  prefix="/product", 
  tags=["product"]
) 
api_router.include_router(
  transaction.router, 
  prefix="/transaction", 
  tags=["trasaction"]
)





