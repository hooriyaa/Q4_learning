
# FastAPI Project

This is a simple FastAPI project for building APIs in Python. FastAPI is a fast and easy-to-use web framework that automatically creates API docs.

## Features

- 🚀 Super Fast: Supports asynchronous code using async/await, making it very efficient.
- 🧩 Easy to Use: Uses Python type hints for automatic validation.
- 📄 Auto Docs: Automatically creates interactive API docs (Swagger UI and ReDoc).
- ✅ Great Developer Experience: Clean syntax, helpful error messages, and built-in testing support.


## Setup Instructions

### Step 1: Check Python Version

Make sure Python is installed. Run this:

```bash
python --version
```

### Step 2: Create Project Folder

```bash
uv init fastdca-p1
cd fastdca-p1
```

### Step 3: Create and Activate Virtual Environment

**On macOS/Linux:**

```bash
uv venv
source .venv/bin/activate
```

**On Windows:**

```bash
uv venv
.venv\Scripts\activate
```

### Step 4: Install Dependencies

```bash
uv add "fastapi[standard]"
```

This installs:

- `fastapi`: The main framework
- `uvicorn`: Runs the app
- `httpx`: For testing APIs

### Step 5: Add Testing Tools

```bash
uv add --dev pytest pytest-asyncio
```

