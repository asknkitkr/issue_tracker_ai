# Version 1: Basic Issue Tracking (Minimal Viable Product - MVP)
A simple Issue Tracker built using **FastAPI**, **Jinja2**, and **Uvicorn**.

## Features
- List all issues on the homepage.
- Create a new issue using a form.
- View issue details using an API endpoint.

---

## 🛠 Installation & Setup

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/yourusername/issue-tracker.git
cd issue-tracker
```

### 2️⃣ Create a Virtual Environment (Recommended)
```sh
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```
---
### 🚀 Running the FastAPI Server
Start the FastAPI server with auto-reload:
```sh
uvicorn main:app --reload
```
- main → Your Python file name (without .py).
- app → The FastAPI app instance.
- --reload → Enables auto-restart on code changes.
- The server will start at: http://127.0.0.1:8000/

## 🖥 API Endpoints
### 1️⃣ Home Page
- **URL:** /
- **Method:** GET
- **Description:** Displays a list of all issues.
  
### 2️⃣ Create Issue
- **URL:** /create_issue/
- **Method:** POST
- **Form Fields:** title, description
- **Description:** Creates a new issue and adds it to the list.
  
### 3️⃣ Get Issue by ID
- **URL:** /api/v1/issue/{issue_id}
- **Method:** GET
- **Description:** Fetches details of an issue by ID.
- **Example:**
```sh
curl -X GET http://127.0.0.1:8000/api/v1/issue/1
```
