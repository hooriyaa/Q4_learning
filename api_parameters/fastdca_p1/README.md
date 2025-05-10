
# 🌟 API Parameters

This project helps to understand how to **receive and check data** in a FastAPI app. FastAPI is a tool used to build websites or apps that can talk to each other through APIs (like a request and answer system).

---

## 📚 Key Concepts Covered

### 1. **Path Parameters**
These are values written inside the URL itself.

For example:
```
/items/5
```
Here, `5` is a **path parameter**. It’s like saying: “Give me item number 5”.

### 2. **Query Parameters**
These are values added after a question mark `?` in the URL.

For example:
```
/items?q=book&skip=0&limit=10
```
- `q=book` is a **search term**.
- `skip=0` means skip 0 items.
- `limit=10` means show 10 items.

### 3. **Request Body**
This is data sent in the form of **JSON** when updating or adding something. It's often used when you send more complex information like:
```json
{
  "name": "Book",
  "description": "A useful book",
  "price": 10.99
}
```

### 4. **Validation**
FastAPI can **check** your data and make sure it is correct before processing it.

Examples:
- A number must be greater than 0.
- A word must have at least 3 letters.
- A field is required or optional.

---

## 🛠️ How to Set Up the Project (Step by Step)

### 1. Create a new project folder
```bash
uv init fastdca_p1
cd fastdca_p1
```

### 2. Create a virtual environment (to keep dependencies clean)
```bash
uv venv
source .venv/bin/activate
```

### 3. Install FastAPI and tools
```bash
uv add "fastapi[standard]"
```

---

## ▶️ How to Run It

Use this command:
```bash
fastapi dev main.py
```

Then go to your browser and open this link:
```
http://localhost:8000/docs
```

You will see an interface where you can test the API easily, without needing to write code.

---

## 🔎 API Endpoints Explained

### 🔹 `GET /items/{item_id}`
You give an item ID (like `5`) in the URL and it returns that item.

FastAPI checks:
- It should be a number.
- It must be **1 or higher**.

---

### 🔹 `GET /items/`
You can send these optional query parameters:
- `q`: a search term like `"shoes"`, must be at least 3 letters.
- `skip`: how many items to skip (default 0).
- `limit`: how many items to return (default 10, max 100).

---

### 🔹 `PUT /items/validated/{item_id}`
You update an item by giving:
- Path parameter: the ID (must be >= 1)
- Query parameter: an optional search term
- Body: A JSON object with name, description, and price

It returns all this information back to you if everything is valid.

---

## 💡 Why This Is Useful

- FastAPI automatically checks the data.
- You get clear error messages if something is wrong.
- You write less code and get better safety.
- It's fast and easy to test.

---


## 🙋‍♀️ About This Project

This was created by **Hooriya Muhammad Fareed** to learn FastAPI step-by-step and help others understand how to build APIs with clean and simple code. ....
