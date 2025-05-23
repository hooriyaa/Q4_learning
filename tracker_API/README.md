
# 📌 Task Tracker API

Welcome to the **Task Tracker API**, a lightweight backend solution built with **FastAPI** and **Pydantic**.

This API helps you manage users and their assigned tasks with clean, simple endpoints for creating, retrieving, and updating records.

---

## 🚀 Project Summary

### ✅ Features:
- Create and manage users.
- Create, retrieve, and update tasks assigned to users.
- Built-in input validation.
- In-memory storage (no database required).
- Swagger UI docs for testing endpoints visually.

---

## 🧩 1. Data Models

### 🧑‍💻 `UserCreate`
- Used for registering a new user.
- Requires:
  - `username` (3–20 characters)
  - `email` (valid format)

### 📥 `UserRead`
- Returned when retrieving user info.
- Includes:
  - `id`
  - `username`
  - `email`

### 📝 `TaskCreate`
- Used to add a new task.
- Requires:
  - `title` (mandatory)
  - `description` (optional)
  - `due_date` (today or future)
  - `user_id` (must exist)

### 🔁 `TaskUpdateStatus`
- Used to update task status.
- `status`: must be one of:
  - `pending`
  - `in_progress`
  - `completed`

### ✅ `Task`
- Complete task object.
- Includes:
  - All TaskCreate fields
  - `id`
  - `status`

---

## 🌐 2. API Endpoints

| HTTP Method | Route                    | Description                             |
|-------------|--------------------------|-----------------------------------------|
| GET         | `/`                      | Returns a welcome message               |
| POST        | `/users/`                | Register a new user                     |
| GET         | `/users/`                | Get all users                           |
| GET         | `/users/{user_id}`       | Get specific user                       |
| POST        | `/tasks/`                | Add a new task                          |
| GET         | `/tasks/`                | Get all tasks                           |
| GET         | `/tasks/{task_id}`       | Fetch a task using its ID               |
| PUT         | `/tasks/{task_id}`       | Update the status of a task             |
| GET         | `/users/{user_id}/tasks` | List all tasks assigned to a user       |

---

## 🛠️ 3. API Walkthrough: Step-by-Step Guide (With Visuals)

This section walks you through how to use the API — from viewing the welcome message to creating users and tasks.

---

### 🔹 Step 0: View the Welcome Message

- Navigate to `http://127.0.0.1:8000/`
- Expected Output:
  
<img width="958" alt="image" src="https://github.com/user-attachments/assets/ff057442-e64b-4d76-b5d8-b0c382e40683" />

---

### 🔹 Step 1: Access Swagger UI

- Go to: `http://127.0.0.1:8000/docs`

<img width="900" alt="image" src="https://github.com/user-attachments/assets/a27b0c29-7d97-4739-be43-d01f04c25d29" />

---

### 🔹 Step 2: Register a User

- Use `POST /users/`
- Provide:
```json
{
  "username": "Hoor",
  "email": "hoor@example.com"
}
```
<img width="917" alt="image" src="https://github.com/user-attachments/assets/e4cc9b78-2e12-4922-a0f9-d2a095c05632" />

<img width="390" alt="image" src="https://github.com/user-attachments/assets/4839a7d6-bb08-45d8-8d6e-cfd330d5f5ea" />

---

### 🔹 Step 3: Add a Task

- Use `POST /tasks/`
```json
{
  "title": "Complete API Project",
  "description": "Write README and finalize",
  "due_date": "2025-05-15",
  "user_id": 1
}
```
<img width="712" alt="image" src="https://github.com/user-attachments/assets/87ff491d-21ec-4bb0-b448-f7f0e3139267" />

<img width="427" alt="image" src="https://github.com/user-attachments/assets/1b856131-6509-45fa-be13-8f8fbcf2547c" />

---

### 🔹 Step 4: Update Task Status

- Use `PUT /tasks/{task_id}`
```json
{
  "status": "completed"
}
```
<img width="628" alt="image" src="https://github.com/user-attachments/assets/be5776bb-08cc-4dca-ab5a-6a0029a09001" />

---

### 🔹 Step 5: View All Tasks for a User

- Use `GET /users/{user_id}/tasks`

<img width="390" alt="image" src="https://github.com/user-attachments/assets/8dae1d1c-8f84-443b-8a07-6c5f8b30c822" />

---

## 🧪 Testing Tips

- Use Swagger UI for trying all endpoints easily.
- Ensure `due_date` is today or later, or it will throw a 422 validation error.
- Only allow status: `pending`, `in_progress`, or `completed`.

---


## 🎯 Conclusion
The **Task Tracker API** is a simple yet powerful tool to manage users and their tasks efficiently.
It lets you:

👥 Create users
- 📝 Assign and track tasks
- 📊 Update task statuses
- 🔗 View user-specific tasks
- 🧪 Test everything via Swagger UI

Perfect for personal projects or team task management systems.
Fast, flexible, and beginner-friendly. ✅

Happy Tracking!🚀
---
