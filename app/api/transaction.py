from fastapi import APIRouter

# instance router ขึ้นมา
router = APIRouter()

@router.get("/transaction")
def get_transaction():
  return{"result":"transaction"}