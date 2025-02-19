# Issue Tracker Backend

```
backend/
│── app/
│   │── api/               # API route definitions
│   │   │── v1/            # Versioned APIs
│   │   │   │── endpoints/ # Routes
│   │   │   │   │── issues.py       # Issue-related routes
│   │   │   │   │── users.py        # User-related routes
│   │   │   │   │── auth.py         # Authentication (JWT)
│   │   │   │── __init__.py
│   │   │── __init__.py
│   │── core/              # Core settings, configs
│   │   │── config.py      # App Configs (SECRET_KEY, DB settings)
│   │   │── security.py    # JWT, Password Hashing
│   │── models/            # Database models
│   │   │── issue.py       # Issue Model
│   │   │── user.py        # User Model (with role field)
│   │── schemas/           # Pydantic Schemas
│   │   │── issue.py       # Issue Schema
│   │   │── user.py        # User Schema
│   │── services/          # Business logic services
│   │   │── issue_service.py
│   │   │── user_service.py
│   │── db/                # Database connection
│   │   │── session.py     # DB Session
│   │   │── base.py        # Base Model
│   │── dependencies/      # Dependency Injection & Security
│   │   │── auth.py        # JWT Auth & Role-based Access Control
│   │   │── db.py          # Database Dependency
│   │── main.py            # FastAPI Entry Point
│── tests/                 # Backend Tests (pytest)
│   │── test_issues.py
│   │── test_users.py
│── requirements.txt       # Python Dependencies
│── alembic/               # Migrations (if using Alembic)
│── Dockerfile             # Backend Dockerfile
```GenAI Integrated Issue Tracker
