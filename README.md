# FastAPI Blog API

A RESTful API built with [FastAPI](https://fastapi.tiangolo.com/) for managing blogs and users. This project demonstrates basic CRUD operations, user authentication (hashing), and database integration using SQLAlchemy.

## Features

### Blog Management
- **Create Blog:** Add new blog posts with titles and bodies.
- **Read Blog:** Retrieve all blogs or a specific blog by ID.
- **Update Blog:** Modify existing blog posts.
- **Delete Blog:** Remove blog posts.

### User Management
- **Create User:** Register new users (passwords are hashed using Bcrypt).
- **Get User:** Retrieve user details by ID.

## Technologies Used

- **Python 3.x**
- **FastAPI**: Modern web framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **PostgreSQL**: Database system (default configuration).
- **Pydantic**: Data validation and settings management.
- **Uvicorn**: ASGI server.

## Prerequisites

- Python 3.7+ installed.
- PostgreSQL installed and running (or modify `database.py` to use SQLite).

## Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd Fastapi-first-api
    ```

2.  **Create a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

The application is currently configured to connect to a PostgreSQL database.

1.  Open `database.py`.
2.  Update the `SQLALCHEMY_DATABASE_URL` or the connection variables (`DB_USER`, `DB_PASS`, `DB_NAME`) to match your local PostgreSQL setup.

    ```python
    # database.py
    DB_USER: str = "postgres"
    DB_NAME: str = "Fastapi"
    DB_PASS: str = "your_password"
    PORT: int = 5432
    ```

    *Note: Ensure the database `Fastapi` (or your chosen name) exists in your PostgreSQL instance.*

## Running the Application

Start the server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## API Documentation

FastAPI provides automatic interactive API documentation. Once the server is running, you can access:

-   **Swagger UI:** `http://127.0.0.1:8000/docs` - Interactive exploration and testing of API endpoints.
-   **ReDoc:** `http://127.0.0.1:8000/redoc` - Alternative documentation visualization.
