# 🌟API Parameters 

This project is made using **FastAPI**, a modern Python web framework. It shows how to receive and validate different types of data in your API using simple and clear examples.

---

## 📌📚 Key Concepts Covered

- ✅ Use **Path Parameters** (data in the URL like `/items/1`)
- ✅ Use **Query Parameters** (data after the `?` in URL like `/items?q=book`)
- ✅ Accept and validate **JSON data** in the request body
- ✅ Add **rules and validation** like minimum/maximum value or length

---

## 🛠️ How to Set Up

### Step 1: Create the project folder

```bash
uv init fastdca_p1
cd fastdca_p1
```

### Step 2: Create a virtual environment

```bash
uv venv
source .venv/bin/activate
```

### Step 3: Install FastAPI

```bash
uv add "fastapi[standard]"
```

---

## 📂 What is in the `main.py` file?

Your main code file has:

1. A GET API that takes an item ID in the path.
2. A GET API that uses query parameters like search, skip, and limit.
3. A PUT API that uses path, query, and body parameters together.

The code also uses **validation**. For example:

- You can make sure a number is greater than 0.
- You can limit the length of a string.
- You can make a parameter optional.

---

## ▶️ How to Run the Server

Run the following command:

```bash
fastapi dev main.py
```

Then open this URL in your browser:

```
http://localhost:8000/docs
```

You will see the **Swagger UI**, a tool where you can test your APIs easily.

---

## 📘 API Overview

### ✅ `GET /items/{item_id}`

- Takes an `item_id` in the URL.
- Makes sure it is a number and greater than or equal to 1.

### ✅ `GET /items/`

- Takes optional query parameters:
  - `q`: search keyword (minimum 3 letters, maximum 50)
  - `skip`: number of items to skip (default: 0)
  - `limit`: number of items to return (default: 10)

### ✅ `PUT /items/validated/{item_id}`

- Takes:
  - `item_id` in the path (must be >= 1)
  - `q` as optional search string
  - A JSON body with item details (name, description, price)

---

## 💡 Notes

- If you send wrong data, FastAPI will show you a clear error message.
- FastAPI uses Pydantic to validate data automatically.

---

## 📚 Learn More

- FastAPI Documentation: [https://fastapi.tiangolo.com](https://fastapi.tiangolo.com)
- Pydantic (data validation): [https://docs.pydantic.dev](https://docs.pydantic.dev)

---

## 🙋‍♀️ About

This project was created by **Hooriya Muhammad Fareed** to learn and share how to work with parameters in FastAPI in an easy way.
