from fastapi import FastAPI, HTTPException,Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import dotenv_values
from bson import ObjectId
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm,OAuth2PasswordBearer
from jose import JWTError, jwt
from datetime import datetime, timedelta

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Task(BaseModel):
    id: str
    text: str
    is_completed: bool = False

class TaskCreate(BaseModel):
    text: str

class Message(BaseModel):
    message: str

class User(BaseModel):
    username: str
    password: str

class UserInDB(User):
    hashed_password: str

    # Password Hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

config = dotenv_values(".env")
client = AsyncIOMotorClient(config["MONGO_URI"])
db = client.todo_database
tasks_collection = db.tasks
users_collection = db.users
# JWT Configuration
SECRET_KEY = "your-secret-key"  
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

async def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise HTTPException(status_code=401, detail="Could not validate credentials")
        user = await users_collection.find_one({"username": username})
    except JWTError:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    if user is None:
        raise HTTPException(status_code=401, detail="Could not validate credentials")
    return user


def task_helper(task) -> dict:
    return {
        "id": str(task["_id"]),
        "text": task.get("text", ""),
        "is_completed": task.get("is_completed", False),
    }

@app.get("/tasks", response_model=List[Task])
async def get_tasks(current_user: dict = Depends(get_current_user)):
    tasks = []
    async for task in tasks_collection.find():
        tasks.append(task_helper(task))
    return tasks

@app.post("/tasks", response_model=Task)
async def add_task(task_create: TaskCreate, current_user: dict = Depends(get_current_user)):
    task_data = {"text": task_create.text, "is_completed": False}
    new_task = await tasks_collection.insert_one(task_data)
    created_task = await tasks_collection.find_one({"_id": new_task.inserted_id})
    return task_helper(created_task)

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, updated_task: Task, current_user: dict = Depends(get_current_user)):
    task_update = await tasks_collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": updated_task.model_dump(by_alias=True, exclude_unset=True)}
    )
    if task_update.modified_count == 1:
        updated_document = await tasks_collection.find_one({"_id": ObjectId(task_id)})
        return task_helper(updated_document)
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Message)
async def delete_task(task_id: str, current_user: dict = Depends(get_current_user)):
    delete_result = await tasks_collection.delete_one({"_id": ObjectId(task_id)})
    if delete_result.deleted_count == 1:
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/signup", response_model=User)
async def signup(user: User):
    existing_user = await users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    hashed_password = get_password_hash(user.password)
    new_user = await users_collection.insert_one({"username": user.username, "hashed_password": hashed_password})
    created_user = await users_collection.find_one({"_id": new_user.inserted_id})
    return {"username": created_user["username"], "password": created_user["hashed_password"]}

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await users_collection.find_one({"username": form_data.username})
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    if not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=400, detail="Incorrect username or password")

    # إنشاء الرمز (Access Token)
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode = {"sub": user["username"]}
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return {"access_token": encoded_jwt, "token_type": "bearer"}


