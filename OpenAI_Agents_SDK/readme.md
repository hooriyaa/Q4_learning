
# 🧠 Getting Started with OpenAI Agents SDK  

AI is evolving fast – and it's no longer just about asking a chatbot simple questions. With **OpenAI's Agents SDK**, we can now build **AI teams** that:

- Work together  
- Share tasks  
- Use tools  
- Follow safety rules  
- Complete complex tasks on their own  

Let’s break it down using real-life examples and easy language.

---

## 🧰 What Is the OpenAI Agents SDK?

The **OpenAI Agents SDK** is an open-source toolkit that lets developers build **agentic AI applications** — systems where multiple AI agents can:

- ✅ Talk to each other  
- ✅ Use tools (like file readers or web search)  
- ✅ Share and delegate tasks  
- ✅ Follow built-in safety rules  
- ✅ Work through multi-step problems — automatically  

🧠 Think of it like building a **team of AI coworkers** that can think and act together.

---

## 🔑 Key Concepts (Explained Simply)

### 1. 🤖 Agents = Smart AI Helpers  
An agent is like a small, intelligent assistant.  
You give it:  
- A role (through “instructions”)  
- Tools (like a calculator or search engine)  
- Some safety rules (called guardrails)  

📌 **Example**:  
You create a **NewsBot** to find and summarize tech news.  
When someone asks, “What’s the latest in AI?”, NewsBot searches online and gives a neat summary.

---

### 2. 🔁 Handoffs = Sharing Tasks Between Agents  
Sometimes, one agent can’t complete the whole job.  
It can **pass the task** to another agent that’s better at that step.

📌 **Example**:  
You say: “Show me a chart of laptop prices.”  
- 🧠 ResearchBot finds the prices  
- 📊 ChartBot draws the chart  

Teamwork – AI style!

---

### 3. 🔐 Guardrails = Safety Rules  
Agents need rules to stay safe and trustworthy.  
**Guardrails help by**:  
- Blocking harmful outputs  
- Controlling which tools the agent can use  
- Ensuring the agent stays "on task"

📌 **Example**:  
You set these rules:  
- ❌ Don’t use unsafe websites  
- ✅ Only summarize trusted content  

---

### 4. 🔎 Tracing = Watching What Agents Do  
The SDK includes **tracing tools** so you can:  
- See every step the agents took  
- Debug any mistakes  
- Improve performance  

📌 **Example**:  
You say: “Plan a 3-day trip to Japan.”  
- ✈️ FlightBot finds flights  
- 🏨 HotelBot picks hotels  
- 📅 PlanBot creates a schedule  

---

## 👩‍💻 What’s Happening Under the Hood?

## ✅ Why is the `Agent` class a `@dataclass`?

In Python, `@dataclass` is a shortcut that makes code shorter and cleaner.

### Why it's used:
- Automatically creates `__init__`, `__repr__`, etc.
- Reduces boilerplate code
- Clearly shows that `Agent` is just a configuration container

### 📌 Think of it like:
Instead of manually filling in all details like a long form, `@dataclass` is like a smart template that does it for you.

### 💡 Example:

```python
# Without @dataclass
class Agent:
    def __init__(self, name, tools, rules):
        self.name = name
        self.tools = tools
        self.rules = rules
```

```python
# With @dataclass
from dataclasses import dataclass

@dataclass
class Agent:
    name: str
    tools: list
    rules: str
```

---

## 📥 What Are "Instructions"?

Instructions are like a **system prompt** — they guide the agent’s behavior.

### 📌 Think of it like:
A job description telling an employee what they should do.

### 💡 Examples:
- `"You are a polite and helpful customer support agent."`
- `"You are a research assistant who gives short summaries."`

You can also **dynamically update** them based on the situation.

### 🔄 Example (Dynamic Instructions):

If the user says:  
> “I want travel advice for Japan”

Then instructions could change to:  
> `"You are a travel agent who only talks about Japan."`

---

## 🧠 What Does `Runner.run()` Do?

The `Runner` class executes the agent’s logic.

### 📌 Think of it like:
A **project manager** assigning tasks and collecting results.

### 💡 What it does:
- Takes user input
- Guides the agent through the task
- Coordinates tool usage
- Returns the final result

### Example:
User asks: “What’s the weather in Paris?”  
`Runner.run()`:
1. Sends this input to the agent
2. Agent uses a weather tool
3. Returns → `"It’s 24°C and sunny in Paris"`

---

## 🔄 What is `TContext` and What Are Generics?

### 🧩 Generics = Smart Containers  
They let you use the **same function or class** with different data types.

### 📌 Think of it like:
One box that can carry either books, clothes, or gadgets — you don’t need a new box every time.

### 💡 Example:

```python
def printer(item):
    print(item)
```

Works for:
```python
printer("Hello")
printer(123)
```

---

### 📦 TContext in the SDK = App-Specific Data

TContext is a flexible data container you can shape based on your app.

### 💡 Examples:
- ✈️ **TravelBot** → `{"destination": "Paris", "budget": "low"}`
- 📰 **NewsBot** → `{"topic": "AI", "length": "short"}`


### 🎯 Benefit:
Write once → Reuse for any agent → Customize as needed!

---

## 🎯 Why Use the OpenAI Agents SDK?

- ✅ Easy to use – even for beginners  
- ✅ Great for big, multi-step apps  
- ✅ Built-in safety and tracing tools  
- ✅ Saves time when building smart workflows  
- ✅ Lets you create **AI teams**, not just chatbots  

---

## 🧩 Final Thoughts  
The OpenAI Agents SDK is a big step forward in AI development.  
Instead of building just **one assistant**, you can build **collaborative AI teams** that solve real problems – like humans in a workplace.  

Whether you’re just starting or already experienced, this SDK is fun, flexible, and full of possibilities.

---

blog link: [https://medium.com/@guujarmahnoor0312/getting-started-with-openai-agents-sdk-building-smart-ai-teams-made-easy-fa265bae1818]

✍️ **Written by:** Hooriya M. Fareed  
👩‍💻 Frontend Developer | Learning AI Systems  
🔗 Follow for more AI, Dev, and Tech stories  
