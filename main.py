from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from models import User, Record
import service, auth

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
def home():
    return FileResponse("templates/index.html")

# USERS
@app.post("/users")
def create_user(user: User):
    return service.create_user(user)

# RECORDS
@app.post("/records/{user_id}")
def add_record(user_id: int, record: Record):
    user = service.get_user(user_id)
    auth.check_role(user, ["ADMIN"])
    return service.add_record(record)

@app.get("/records/{user_id}")
def get_records(user_id: int):
    user = service.get_user(user_id)
    auth.check_role(user, ["ADMIN","ANALYST","VIEWER"])
    return service.get_records()

# SUMMARY
@app.get("/summary/{user_id}")
def summary(user_id: int):
    user = service.get_user(user_id)
    auth.check_role(user, ["ADMIN","ANALYST"])
    return service.get_summary()

@app.get("/summary/category/{user_id}")
def category(user_id: int):
    user = service.get_user(user_id)
    auth.check_role(user, ["ADMIN","ANALYST"])
    return service.get_category_summary()

@app.get("/summary/trends/{user_id}")
def trends(user_id: int):
    user = service.get_user(user_id)
    auth.check_role(user, ["ADMIN","ANALYST"])
    return service.get_trends()