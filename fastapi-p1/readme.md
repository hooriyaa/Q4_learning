# 🚀 FastAPI Project — `fastdca-p1`

Welcome to `fastdca-p1`, a FastAPI-based project designed to help you quickly build modern, high-performance APIs in Python. FastAPI is built on top of Starlette and Pydantic, offering asynchronous support, automatic documentation, and strong data validation out of the box.

---

## ⚙️ Key Features

- **⚡ Fast Performance** – Powered by Starlette and optimized for async.
- **✅ Easy to Use** – Simple Python syntax and automatic request validation.
- **📄 Auto Docs** – Comes with Swagger and ReDoc interfaces built-in.
- **🧪 Testing Ready** – Easily testable with built-in HTTP client and pytest support.

---

## 📦 Getting Started

Follow these steps to set up and run your FastAPI project using [`uv`](https://github.com/astral-sh/uv):

---

### ✅ Step 1: Check Python Version

Make sure Python is installed (Python 3.11+ recommended):

```bash
python --version
```

---

### 📁 Step 2: Initialize the Project

Create a new project and enter the directory:

```bash
uv init fastdca-p1
cd fastdca-p1
```

---

### 🐍 Step 3: Create & Activate Virtual Environment

**On Windows:**

```bash
uv venv
.venv\Scripts\activate
```

**On macOS/Linux:**

```bash
uv venv
source .venv/bin/activate
```

---

### 📥 Step 4: Add Dependencies

Install FastAPI and the required packages:

```bash
uv add "fastapi[standard]"
```

This installs:

- `fastapi` – The web framework
- `uvicorn` – The ASGI server to run your app
- `httpx` – A powerful HTTP client for testing APIs

Add development dependencies for testing:

```bash
uv add --dev pytest pytest-asyncio
```

---

## 📄 Example API (`main.py`)

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}
```

---

## 🚀 Run the Server

**Option 1: Use FastAPI CLI**

```bash
fastapi dev main.py
```

**Option 2: Use Uvicorn directly**

```bash
uv run uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 🌐 Test Your API

- Root endpoint: [http://localhost:8000](http://localhost:8000)
- Item endpoint: [http://localhost:8000/items/5?q=sample](http://localhost:8000/items/5?q=sample)

### 📘 Interactive Docs

- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)
- ReDoc: [http://localhost:8000/redoc](http://localhost:8000/redoc)

---

## ✅ What's Next?

- Add new API routes
- Integrate database support (PostgreSQL, SQLite, etc.)
- Implement business logic and validations
- Write unit tests using `pytest`

---

## 🧾 License

This project is licensed under the MIT License.

---

> Built with ❤️ using FastAPI

