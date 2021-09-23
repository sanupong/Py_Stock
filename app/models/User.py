import datetime
from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.sql.expression import column
from .database import Base

class User(Base):
  __tablename__ = "users"   #Variable ไว้เก็บชื่อ Table 

  id = Column(Integer, primary_key=True)
  username = Column(String(100), unique=True)
  password = Column(String(100))
  level = Column(String(100), default="normal")
  create_at = Column(DateTime, default=datetime.datetime.utcnow)

  class Config:
    arbitrary_types_allowed = True #อนุญาตให้ส่ง Type ที่ไม่ต้องตรงกันมากนักได้ไหม
  