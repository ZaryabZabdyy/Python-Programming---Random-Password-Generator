# 📊 Zabdy's Expense Tracker – Smart Financial Management 

A secure, minimalist Full-Stack Web Application designed to help multiple users seamlessly register, login, track, and categorize their daily financial expenses with direct relational data persistence.

---

## ✨ Key Features

* **🔒 Multi-User Authentication:** Secure Signup and Login interfaces. Every user gets a private environment where access token validations are enforced.
* **💾 Relational Data Persistence:** Structured storage powered by **SQLite Engine** mapping accounts directly to items via physical relational bindings.
* **📂 Structured Expense Categorization:** Categorize spending inputs instantly through drop-down indicators (Food, Travel, Bills, Education, Entertainment).
* **⏰ Automatic Smart Timestamps:** Every transaction tracks real-time generation metrics, sorting history lists seamlessly by *Latest First*.
* **🗑️ Complete CRUD Capabilities:** Integrated Create, Read, and Dynamic Row-Level Deletion actions running instant asynchronous requests.

---

## 🏗️ Simple Database Schema

The persistence architecture consists of **two tables** managing a relational **1-to-Many Relationship** (One User can own multiple separate expenses):

### 1. Users Table
| Column Name | Data Type | Key / Constraint |
| :--- | :--- | :--- |
| `User_ID` | INTEGER | PRIMARY KEY (Auto Increment) |
| `username` | TEXT | UNIQUE, NOT NULL |
| `Password` | TEXT | NOT NULL |

### 2. Expenses Table
| Column Name | Data Type | Key / Constraint |
| :--- | :--- | :--- |
| `Expense_ID`| INTEGER | PRIMARY KEY (Auto Increment) |
| `description`| TEXT    | NOT NULL |
| `amount`     | REAL     | NOT NULL |
| `category`   | TEXT     | NOT NULL |
| `created_at` | DATETIME | DEFAULT CURRENT_TIMESTAMP |
| `User_ID`    | INTEGER  | FOREIGN KEY ➔ `Users(User_ID)` |

---

## 🛠️ Project Tech Stack

* **Frontend:** HTML5, Modern Dashboard Vanilla CSS3, Javascript (Fetch API Context)
* **Backend Environment:** Node.js, Express.js Framework
* **Database Management:** SQLite3 Engine (Zero External Installation Needed)

---

## 🚀 How to Run the Project (Quick Start Guide)

You can launch the environment easily using either the standard developer automation scripts or the 1-click execution sequence.

### Method 1: The Automated 1-Click Method (Highly Recommended)
1. Navigate directly inside the cloned repository root folder.
2. Locate the automation script named **`run.bat`**.
3. **Double-click** the file. A background processing window will initialize the server engine and open the application inside your default browser instantly.

### Method 2: The Manual Terminal Method
If you prefer running configuration files explicitly inside a terminal context, use these structural setup sequences:

1. Open your terminal workspace inside the project directory root path.
2. Run the deployment setup script to assemble runtime libraries:
   ```bash
   npm install
