from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, constr, validator
from datetime import date
from typing import Optional, List

# ✅ Create a FastAPI app instance
app = FastAPI(
    title="📌 Task Tracker API",
    description="API to manage Users and their Tasks efficiently.",
    version="1.0.0"
)

# ✅ Root route for welcome message
@app.get("/")
def read_root():
    return {
        "message": "👋 Welcome to the Task Tracker API!",
        "info": "Use this API to manage users and their tasks.",
        "docs": "Visit /docs to see all available endpoints."
    }

# ✅ In-memory data storage (global dictionaries)
USERS: dict[int, dict] = {}
TASKS: dict[int, dict] = {}
user_id_counter = 1
task_id_counter = 1

# ✅ Pydantic models for user
class UserCreate(BaseModel):
    username: str  # username must be 3–20 chars

    @validator("username")
    def validate_username(cls, v):
        if not (3 <= len(v) <= 20):
            raise ValueError("Username must be between 3 and 20 characters")
        return v
    email: EmailStr  # validate email format

class UserRead(BaseModel):
    id: int
    username: str
    email: EmailStr

# ✅ Pydantic models for task
class Task(BaseModel):
    id: int
    title: str
    description: Optional[str]
    due_date: date
    status: str
    user_id: int

    # ✅ Validate that due_date is today or in the future
    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    due_date: date
    user_id: int

    # ✅ Reuse the due_date validator
    @validator("due_date")
    def validate_due_date(cls, v):
        if v < date.today():
            raise ValueError("Due date cannot be in the past")
        return v

class TaskUpdateStatus(BaseModel):
    status: str

    # ✅ Only allow certain status values
    @validator("status")
    def validate_status(cls, v):
        allowed_statuses = {"pending", "in_progress", "completed"}
        if v not in allowed_statuses:
            raise ValueError("Status must be one of: pending, in_progress, completed")
        return v

# ✅ Create a new user
@app.post("/users/", response_model=UserRead)
def create_user(user: UserCreate):
    global user_id_counter
    user_data = user.dict()
    user_data["id"] = user_id_counter
    USERS[user_id_counter] = user_data
    user_id_counter += 1
    return user_data

# ✅ Get a user by ID
@app.get("/users/{user_id}", response_model=UserRead)
def get_user(user_id: int):
    user = USERS.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# ✅ Get all users
@app.get("/users/", response_model=List[UserRead])
def list_users():
    return list(USERS.values())

# ✅ Create a new task
@app.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    global task_id_counter
    if task.user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    task_data = task.dict()
    task_data["id"] = task_id_counter
    task_data["status"] = "pending"  # default status
    TASKS[task_id_counter] = task_data
    task_id_counter += 1
    return task_data

# ✅ Get a task by ID
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task

# ✅ Update a task's status only
@app.put("/tasks/{task_id}", response_model=Task)
def update_task_status(task_id: int, status_update: TaskUpdateStatus):
    task = TASKS.get(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    task["status"] = status_update.status
    return task

# ✅ Get all tasks for a specific user
@app.get("/users/{user_id}/tasks", response_model=List[Task])
def get_user_tasks(user_id: int):
    if user_id not in USERS:
        raise HTTPException(status_code=404, detail="User not found")

    user_tasks = [task for task in TASKS.values() if task["user_id"] == user_id]
    return user_tasks

# ✅ Get all users
@app.get("/users/", response_model=List[UserRead])
def get_all_users():
    return list(USERS.values())

# ✅ Get all tasks  
@app.get("/tasks/", response_model=List[Task])
def get_all_tasks():
    return list(TASKS.values())



