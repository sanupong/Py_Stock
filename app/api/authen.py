from app.models.database import SessionLocal
from fastapi import APIRouter, Depends
from app.api import schema
from app.db import get_db
from sqlalchemy.orm import Session
from app.models.User import User as UserDB
from app.api import security

# instance router ขึ้นมา
router = APIRouter()


@router.get("/authen")
def get_authen():
	return{"result":"authen"}

@router.post("/register")
def register(user:schema.User, db: Session = Depends(get_db)):
	try:		
		user_db = UserDB(
			username=user.username, 
			password=security.get_password_hash(user.password)
		)
		db.add(user_db)
		db.commit()
		return {"result": "OK"}
	except Exception as e:
		return {"result": "register fails", "error": "duplicate username"}

@router.post("/login")
def login(user:schema.User, db: Session = Depends(get_db)):
	try:
		user_db = db.query(UserDB).filter(UserDB.username == user.username).first()
		# verify username
		if not user_db:
			return {"result": "Error", "error": "invalide username"}

		# verify password
		if not security.verify_password(user.password,user_db.password):
			return {"result": "Error", "error": "invalide password"}

		# login success
		return {"Login": "OK" }
	except Exception as e:
		return {"Login": "nok", "error": e }
