## 📘 What is Pydantic?

**Pydantic** is a Python library used for:

✅ Data validation  
✅ Type checking  
✅ Automatic conversion of data  
✅ Handling complex/nested data structures  
✅ Clear error messages when data is incorrect  

It uses Python type hints to ensure your data is correct. It's very useful when building APIs with FastAPI, because it helps validate user input and return structured responses.

---

## 🔍 Why Use Pydantic?

- 🔐 Ensures **data integrity**
- 🧠 Supports **complex data models**
- 🔄 Converts data automatically (e.g., `"123"` to `123`)
- 🚫 Catches errors early with clear messages
- 🌐 Great for **API development** and **AI workflows**

---

## 🛠️ Project Setup

```bash
# Create and enter project
uv init fastdca_p1
cd fastdca_p1

# Setup virtual environment
uv venv
source .venv/bin/activate

# Install FastAPI and standard dependencies
uv add "fastapi[standard]"
```

---

## 📂 Files in This Project

### `pydantic_example_1.py`
Basic model usage, validation, and error handling.

### `pydantic_example_2.py`
Nested models (e.g., user with multiple addresses).

### `pydantic_example_3.py`
Custom validator to check user name length.

### `main.py`
Full FastAPI app simulating a chatbot with message and metadata models.

---

## ▶️ Running the Code

### Run Example Scripts

```bash
uv run python pydantic_example_1.py
uv run python pydantic_example_2.py
uv run python pydantic_example_3.py
```

### Start FastAPI Server

```bash
fastapi dev main.py
```

Then open [http://localhost:8000/docs](http://localhost:8000/docs) to test the chatbot API.

## 🙌 Final Words

Pydantic makes your code **cleaner**, **safer**, and **more reliable** – especially when working with APIs.

Explore the files, run the code, and start building smarter Python applications! 🎉
