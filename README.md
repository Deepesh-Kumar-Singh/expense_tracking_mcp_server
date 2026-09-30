# 💰 Expense Tracker MCP Server

An **MCP (Model Context Protocol) based Expense Tracker** that allows you to manage and analyze your expenses using AI assistants such as **Claude Desktop**.

The server provides tools to:

* ➕ Add new expenses
* 📋 List expenses within a date range
* 📊 Summarize expenses by category
* 🗂️ Access available expense categories
* 💾 Store expense data in an SQLite database

---

## 🚀 Features

### ➕ Add Expense

Add an expense with:

* Date
* Amount
* Category
* Subcategory
* Note

Example:

```text
Date: 2026-09-30
Amount: ₹500
Category: Food & Dining
Subcategory: Restaurant
Note: Dinner with friends
```

### 📋 List Expenses

Retrieve expenses between two dates.

Example:

```text
Start Date: 2026-09-01
End Date: 2026-09-30
```

### 📊 Expense Summary

Get a summary of expenses grouped by category.

Example:

```text
Food & Dining       ₹5,200
Transportation      ₹2,100
Shopping            ₹3,500
Entertainment       ₹1,200
```

You can also summarize expenses for a specific category.

---

# 🏗️ Project Structure

```text
Expense-Tracker/
│
├── expense_tracker.py
├── expenses.db
├── categories.json
├── requirements.txt
└── README.md
```

> **Note:** `expenses.db` may be created automatically when the server starts.

---

# 🛠️ Technologies Used

* 🐍 Python
* 🔌 FastMCP
* 🗄️ SQLite
* ⚡ aiosqlite
* 🤖 Model Context Protocol (MCP)
* 💻 Claude Desktop

---

# ⚙️ Local Installation

## 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project directory:

```bash
cd Expense-Tracker
```

---

## 2. Create a virtual environment

### Windows

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

---

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

If you don't have a `requirements.txt`, install the required packages:

```bash
pip install fastmcp aiosqlite
```

---

# ▶️ Run the MCP Server Locally

Run:

```bash
python expense_tracker.py
```

The server will start using HTTP transport.

Example:

```text
http://localhost:8000
```

---

# ☁️ Connect the Deployed MCP Server to Claude Desktop

You can connect the deployed Expense Tracker MCP server to Claude Desktop using a **Custom Connector**.

## Step 1 — Open Claude Desktop

Open the **Claude Desktop application** on your computer.

---

## Step 2 — Open Connectors

Click the **`+` button** in Claude Desktop.

Then select:

```text
Connectors
```

---

## Step 3 — Add Custom Connector

Click:

```text
Add custom connectors
```

---

## Step 4 — Enter Connector Information

Enter a name for your connector.

For example:

```text
Expense Tracker
```

Then paste your deployed MCP server URL.

Example:

```text
https://expense-tracking-mcp-server.onrender.com
```

> Replace the URL above with your actual deployed server URL.

Then click:

```text
Add
```

---

## Step 5 — Continue

After adding the connector, click:

```text
Continue
```

---

## Step 6 — Select Authentication

When Claude asks for authentication, select:

```text
No Authentication
```

Then click:

```text
Add
```

---

## Step 7 — Refresh Claude Desktop

Refresh or restart your Claude Desktop application.

Your MCP server should now appear as an available connector.

🎉 **Your Expense Tracker is now connected to Claude Desktop!**

---

# 🤖 Using the Expense Tracker with Claude

Once connected, you can interact with your expenses using natural language.

For example:

### Add an expense

```text
Add ₹500 expense for dinner today under Food & Dining.
```

Claude can use the Expense Tracker MCP server to add the expense.

### View expenses

```text
Show me all my expenses from September 1 to September 30.
```

### Get a summary

```text
Give me a summary of my expenses for September.
```

### Category-specific summary

```text
How much did I spend on transportation this month?
```

### Analyze spending

```text
Which category did I spend the most money on this month?
```

---

# 🔌 Available MCP Tools

| Tool            | Description                           |
| --------------- | ------------------------------------- |
| `add_expense`   | Adds a new expense                    |
| `list_expenses` | Lists expenses within a date range    |
| `summarize`     | Summarizes expenses by category       |
| `categories`    | Provides available expense categories |

---

# 📂 Expense Categories

The default categories include:

```text
Food & Dining
Transportation
Shopping
Entertainment
Bills & Utilities
Healthcare
Travel
Education
Business
Other
```

You can modify `categories.json` to customize the available categories.

---

# 🗄️ Database

The project uses **SQLite** for storing expenses.

The database contains the following fields:

| Field         | Description            |
| ------------- | ---------------------- |
| `id`          | Unique expense ID      |
| `date`        | Expense date           |
| `amount`      | Expense amount         |
| `category`    | Main expense category  |
| `subcategory` | Expense subcategory    |
| `note`        | Additional information |

---

# 🌐 Deployment

The MCP server can be deployed to cloud platforms such as **Render**.

After deployment, use the deployed MCP endpoint when creating the custom connector in Claude Desktop.

Example:

```text
https://expense-tracking-mcp-server.onrender.com
```

Make sure your deployed server is publicly accessible and running before connecting it to Claude Desktop.

---

# 🔐 Authentication

This project currently uses:

```text
No Authentication
```

This makes it easy to connect with Claude Desktop.

> ⚠️ If you deploy this publicly, consider adding authentication before using it with sensitive or personal financial data.

---

# 🔄 How It Works

```text
        User
          │
          ▼
   Claude Desktop
          │
          │ MCP
          ▼
   Expense Tracker
      MCP Server
          │
          ▼
      SQLite DB
          │
          ▼
      Expense Data
```

---

# 🎯 Future Improvements

Some possible improvements for the project:

* 🔐 Authentication
* 🐘 PostgreSQL database for cloud deployment
* 📈 Expense visualization
* 📊 Monthly and yearly reports
* 💰 Budget tracking
* 🔔 Budget alerts
* 📱 Web dashboard
* 📤 CSV/PDF export
* 🤖 AI-based spending recommendations
* 👥 Multi-user support

---

# 👨‍💻 Author

**Deepesh Kumar Singh**

B.Tech Computer Science & Engineering (AI)

---

# ⭐ Support

If you find this project useful, consider giving the repository a ⭐ on GitHub!

Feel free to fork the project and improve it.

---

## 📜 License

This project is open-source and available under the terms of the license included in this repository.
