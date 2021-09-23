ep1 intro
- pip3 install pipenv aiofiles
- pipenv shell
- pipenv install fastapi sqlalchemy pydantic 
ep2 setup fastapi
- สร้าง Folder App เพื่อบรรจุ main app และทำให้ folder app เป็นแบบ Modeul โดยสร้าง __init__.py 
- สร้าง main.py import fastapi แล้วลอง Run uvicorn app.main:app --reload [--port 8081]
- ประกาศ route ไว้สักหนึ่งอัน @app.get()
ep3 setup rounter
- สร้าง subfolder api และสร้าง init file เพื่อให้เป็น Module
- สร้าง file .py ขึ้นมาพวก authen.py, product.py, transaction.py
- สร้างไฟล์ version เช่น v1.py เพื่อไว้ระบุ api router เพื่อไปเรียกไฟล์ต่าง ๆ ตาม router ที่ระบุไว้ ซึ่ง main จาก folder app จะมาเรียก v1.py และ v1.py จะไปเรียกไฟล์อื่น ๆ ตาม router ที่กำหนด
- v1.py จะ import fastapi router เข้ามา
- ก่อนจะ Include ฟังก์ชันต่าง ๆ ของแต่ละ Module ก็จะต้อง import module นั้น ๆ เข้ามาก่อน ก็จะเรีย from app.api import [ชื่อ Moduleต่าง ๆ ]
- ที่นี้แต่ละ module ก็จะไปสร้าง router เพิ่มเติมเพื่อทำงานแต่ละละ module ไป ก็จะเขียน code คล้าย ๆ v1.py 
- โยก get("/") ที่อยู่ที่ main.py มาไว้ที่ authen.py แทน และเปลี่ยนเป็น router.get("/authen")
- copy ทั้งหมดใน authen ไปใส่ใน product, transaction และเปลี่ยนชื่อให้สอดคล้องกับ module นั้น ๆ  เพื่อดูว่าจะกระจาย route ได้จริงไหม
- แก้ชื่อไฟล์เป็น v2.py (เนื่องจาก front-end เรียกที่ไฟล์นี้)
- ไปที่ main เพื่อเรียก v2.py โดยการ from app.api.v2 import api_router และ app.include_router เข้ามา
- ลอง Run แล้วเรียกดู 
ep4 setup static folder
- สร้าง folder uploaded และ subfolder images
- set share static folder โดยการ mount folder (ไม่ควร mount root folder และควรระวัง) ใน path ของ images 
- ไปที่ main.py และ import module fastapi staticfiles *แต่ต้องติดตั้ง pipenv install aiofiles ก่อน
- run uvicorn app.main:app --reload
ep5 vscode setting tabwidth and format
- สร้าง subfolder .vscode > สร้างไฟล์ settings.json 
ep6 intro pydantic and register
- install vscode extension rest client
- สร้างไฟล์ curl.http [จริง ๆ ชื่อไฟล์อะไรก็ได้ แต่ต้องมีนามสกุลเป็น http] ไว้จำลอง request ในการทดสอบ
- ไปที่ authen.py เพื่อสร้าง router ใหม่ ชื่อว่า register 
  - from pydantic import BaseModel
  - from typing import Optional
  - สร้าง class User()
  - สร้าง router POST register แล้ว return 
  - copy curl จาก swagger doc มาใส่ใน curl.http ไฟล์ และลองกด send request จะได้ echo api กลับมาไว้สำหรับทดสอบได้
ep7 create data class schema file
- เป็นการโยก Code ของพวก Data Class ไว้ไฟล์ต่างหาก
- กลับไปปรับ authen.py โดยเริ่มที่ from app.api import schema
- เวลาเรียกใช้ เราก็เรียก schema.User ได้เลย เพื่อไม่ให้สับสน หากมีการประกาศ User จากเรื่องอื่นด้วย
ep8 prefix router
- ที่ authen.py เพื่อ route login เข้ามา
- ที่ v2.py เราจะไปใส่ prefix ให้กับ router 
   - ไปที่ product.py ไปสร้าง route หลัก ๆ ก่อน โดย copy code จาก authen ไปปรับปรุง
   - ที่ v2.py function include_router สามารถใส่ prefix เข้าไปได้
   - ทำที่ include router ของ transaction เช่นเดียวกัน
ep9 Depends วางโครงสร้างบันทึกลง DB ด้วย SQLalchemy
- อธิบาย Concept ของ Depends ให้ไปที่ authen.py แล้ว import Depends เพื่อมาใน from fastapi ต่อท้าย APIRouter
- สร้าง function d1() return "Hey" และไปที่ router register เพิ่ม paramter เป็น msg: str = Depends(d1) แล้วเพิ่ม print("Register is called" + msg)
* Depends เป็นการ Inject ผลลัพธ์ ที่ได้จาก Function เข้าไป
ep10 Database Integration 1
- สร้าง Folder models , สร้าง __init__.py เพื่อบอกว่า models เป็น Module, สร้าง database.py, Product.py, Transaction.py, User.py
- สร้างไฟล์ db.py ไว้ที่ folder app
- ที่ไฟล์ database.py ใน Folder main ให้ copy code มาใส่เลย
- ที่ไฟล์ User.py ให้ import datetime, sqlalchemy, .database มาจากต้นแบบได้เลย
- สร้าง class model User(Base)
- กลับไปที่ Authen.py ลบ Depends d1 ทิ้ง
    - เพิ่ม from app.db import get_db ที่ Depends(d1) เดิม เปลี่ยนเป็น Depends(get_db)
    - ให้ไปเพิ่ม Code ที่ db.py
    - กลับมาที่ authen.py เปลี่ยน msg = db และ str = Session
    - import from sqlalchemy.orm import Session
    - pip3 install sqlalchemy ถ้า run uvicorn แล้ว error
ep11 Insert User into database
- ติดตั้ง Extension เพิ่มชื่อว่า SQLite
- ไปที่ v2.py เพื่อไป Load เรียก Database instance ที่ database.py
- import from app.models import database
- database.Base.metadata.create_all(database.engine, checkfirst=True)
- หากเรียก uvicorn อยู่ จะเป็น auto reload ก็จะเห็นว่ามี ไฟล์ cmstock.db เกิดขึ้นมาที่ root folder
- จากนั้นไปที่ authen.py เพื่อไปกำหนดให้ทุกครั้งที่มีการ register เข้ามาให้บันทึกลง DB
   - import from app.models.User import User as UserDB (มีการ cast ชื่อด้วย)
   - ที่ router register ให้ปรับปรุง Code
   - เมื่อ Run Code จะเห็นว่ามี Table เพิ่มขึ้นมาเลย เพราะเรา Reload ด้วย uvicorn
   - ลองยิง curl.http ไฟล์ send request register ดู
   - ไป show table ที่ table users จะเห็นว่ามีข้อมูลมาแล้ว
ep12 Hass Password
- สร้างไฟล์ security.py ไว้ที่ api folder
- import from passlib.context import CryptContext
- import from typing import Optional
- import from datetime import datetime, timedelta
- มีการเอาความรู้จาก FAST_API_Demo18 เรื่องการ hash Login and Register อย่างง่ายด้วย PassLib
    - มี function verify_password, get_password_hash    
- ติดตั้ง passlib[bcrypt] โดยออกจาก pipenv shell ก่อนด้วย exit แล้วพิมพ์ pip3 install "passlib[bcrypt]"
- ที่ไฟล์ authen.py import security ไฟล์ module เข้ามา from app.api import security
- ใช้งาน hash password ไปที่ router register ตรงส่วนที่เป็น password ให้ครอบ function security.get_password_hash
- ลองเรียกผ่าน curl.http จะเห็นว่า password จะถูก encrypt แล้ว
- ที่ router register ตรง return ให้เปลี่ยนจาก return user เป็น return {"register": "OK"}
ep13 add query for login
- ไปที่ไฟล์ authen.py เพื่อ pass Depends เข้าไปที่ function login ใน router login
- try
   - สร้างตัวแปรรับค่า query user
   - เขียน Code verify username, verify password, login success
   - except กรณี error 
   - test ที่ curl.http ได้
ep14 set unique to username 
- ลบ cmstock.db ออกไปก่อน
- ไปที่ไฟล์ User.py เพื่อไปเปลี่ยนแปลงโครงสร้าง Table users ให้ Field username เป็น unique
- ไปที่ไฟล์ authen.py แก้ Code register เช็ค try catch เพื่อไม่ให้ Error เวลา add user
git add . && git commit -m "ep2 - ep14" && git push
ep15 insert product using url encoded form























