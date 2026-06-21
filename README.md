# Rocket Flight Manager Backend

A restful backend application for managing rocket flight test records. The project provides secure user authentication and complete CRUD operation for storing ,retrieving, updating and deleting rocket flight test information.

----
## Features 
- User Registration and Authentication with bcrypt password hashing
- Create Flight test records
- Retrieve All Flight tests
- Retrieve Flight tests by id
- Update Flight test records
- Delete Flight test records
- Request and Response Validation using Pydantic

---

## Tech Stack
- Python
- FastAPI
- PostgresSQL
- Passlib(bcrypt)
- Uvicorn
- SQLAlchemy ORM
- Pydantic

---

## Project Structure

```
backend/
|
|_ app/
|  ├── main.py
|  ├── models.py
|  ├── schemas.py
|  ├── crud.py
|  ├── database.py
|  ├── auth.py
|  ├── dependencies.py
|
├── requirements.txt
├── README.md
└── .gitignore
```
---

## API Endpoints

### Authentication

| Method | Endpoint | Description |
|----|----|---|
| POST | /register| Register a new user |
| POST | /login| Autheticate a existing user |

### Flight Tests

| Method | Endpoint | Description |
|----|----|---|
| POST | /flight-tests| Create a flight test |
| GET | /flight-tests| Retrieve all flight tests |
| GET | /flight-tests/{id}| Retrieve flight test by ID |
| PUT | /flight-tests/{id} | Update a flight test |
| DELETE | /flight-tests/{id}| Delete a flight test |

---

## Database Design

**User**
- id
- name
- username
- email
- password_hash

**Flight Test**
- id
- launch_date
- rocket_name
- rocket_weight
- launch_angle
- no_of_motors
- thrust
- status
- reason
- owner_id
- created_at

**Relationship :** One User -> Many Flight tests

---

## Installation

1. **Clone Repsitory**

    git clone ```https://github.com/Sandysoil2115/rocket-flight-test-manager.git```

2. **Create a Virtual Environment**
    ```
    python -m venv venv
    ```
3. **Activate the Virtual Environment**
    ```
    Linux/macOS

    source venv/bin/activate

    Windows

    venv\Scripts\activate
    ```
4. **Install Dependencies**

    ```pip install -r requirements.txt ```

5. **Create PostgresSQL Database**

    ```CREATE DATABASE rocket_flight_manager;```

6. **Configure Database Connections**

    Update database URL in app/database.py

    ```DATABASE_URL = "postgresql://username:password@localhost:5432/rocket_flight_manager"```

7. **Create Database Table**

    execute : ```Base.metadata.create_all(bind=engine)```

8. **Start the Server**

    go to the directory backend and execute:

    ```
    uvicorn app.main:app --reload
    ```
    The API will be available at :
    ```
    http://127.0.0.1:8000
    ```

9. **Open API Documentation**

    Swagger UI:
    ```
    http://127.0.0.1:8000/docs
    ```
    
