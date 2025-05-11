# 📘 FastAPI Dependency Injection

## 🌟 What is Dependency Injection?

Dependency Injection (DI) is a way to **organize your code** better.

Imagine you are writing the same code again and again (like checking if a user is logged in, or getting data from a database). Instead of repeating this code in every API route, you can move it into a separate function.

Then, you tell FastAPI to "inject" that function into any route where you need it. This keeps your code **clean**, **short**, and **easy to manage**.

FastAPI helps you do this using `Depends()`.

---

## ✅ Why Should We Use It?

- **Reuse Code**: No need to write the same thing in every route.
- **Keep It Simple**: Your route will only have important logic.
- **Easy Testing**: You can use fake/mock data during testing.
- **Better Structure**: Your code will be neat and professional.

---

## ⚙️ How Does It Work?

1. **Write a function** (or class) that does something – like checking login info.
2. In your route, add that function using `Depends()`.
3. FastAPI will call that function **before** your main route logic runs.
4. You can also use `Annotated` to make it look cleaner and easier to read.

FastAPI even remembers the result of the function during the same request, so it doesn't run it again and again.

---

## 🔍 Examples (Explained Simply)

### 1. Simple Goal Message

You make a function that returns a message like “We are building AI Agents.”  
Then, in your API route, you use this function using `Depends()`.  
Result: Every time someone visits the route, they see that message.

### 2. Goal with Username

This function takes a query like `?username=Ali` and returns a message with the username.  
It shows how dependencies can use input parameters.

### 3. Login Check

Here, the function checks if username and password are "admin".  
If yes, it returns “Login Successful”, otherwise “Login Failed”.  
Very useful for authentication.

### 4. Two Functions Together

You use two functions in the same route.  
Each one does a calculation (like adding 1 or 2 to a number).  
FastAPI runs both and gives you the results in your route.

### 5. Class as Dependency

This is useful when you want to simulate a database.  
The class checks if a blog ID or user ID exists in a dictionary.  
If the ID doesn’t exist, it returns a 404 error.

This is very helpful when you want to fetch data from a database or check if something exists.

---

## 📌 Final Thoughts

- Use Dependency Injection to **keep your code clean** and **organized**.
- You can use **functions** or **classes** as dependencies.
- Use `Depends()` to tell FastAPI to run those dependencies.
- Perfect for common tasks like login checks, database fetches, etc.
- FastAPI handles everything for you – you just plug in your dependency.

👍 That's how you can write better and smarter APIs with FastAPI!


