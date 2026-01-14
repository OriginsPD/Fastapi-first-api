# Project Context: FastAPI Blog API

## Overview
This is a Python-based REST API built using the **FastAPI** framework. It implements a simple blogging system where users can create, read, update, and delete blogs. The project follows a structured architecture, separating concerns into routers, repositories, models, and schemas.

## Architecture & Technologies
*   **Framework:** FastAPI
*   **Database:** PostgreSQL (configured in `database.py` as `postgresql://postgres:MADman123@localhost:5432/Fastapi`).
*   **ORM:** SQLAlchemy
*   **Data Validation:** Pydantic
*   **Server:** Uvicorn
*   **Authentication/Security:** Basic password hashing using `hashing.py` (likely bcrypt).

### Directory Structure
*   `main.py`: Application entry point. Initializes the app and includes routers.
*   `database.py`: Database connection setup and session management.
*   `models.py`: SQLAlchemy database models (`Blog`, `User`).
*   `schemas.py`: Pydantic models for request validation and response serialization.
*   `routers/`: Contains API route definitions (`blog.py`, `user.py`).
*   `repository/`: Abstraction layer for database operations (currently implemented for `blog.py`).
*   `hashing.py`: Utility for password hashing.

## Setup & Running

### Prerequisites
*   Python 3.x
*   PostgreSQL running locally (or adjust `database.py`).
*   Virtual environment (recommended).

### Installation
1.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Running the Application
The application uses Uvicorn as the ASGI server.
```bash
uvicorn main:app --reload
```
*   The API will be available at `http://127.0.0.1:8000`.
*   Interactive documentation (Swagger UI) is available at `http://127.0.0.1:8000/docs`.

## Development Conventions
*   **Repository Pattern:** The project attempts to use the Repository pattern (seen in `repository/blog.py`) to decouple business logic from the API routes. However, `routers/user.py` currently interacts with the DB directly.
*   **Dependency Injection:** Database sessions are managed using FastAPI's dependency injection (`Depends(get_db)`).
*   **Response Models:** Pydantic models are used as `response_model` in decorators to filter and format output data.

## TODOs / Observations
*   **Inconsistency:** The user router (`routers/user.py`) does not use the repository pattern, unlike the blog router. It interacts directly with the database.
*   **Hardcoded Credentials:** Database credentials in `database.py` are hardcoded. Consider moving these to environment variables (`.env`).
*   **User ID:** In `repository/blog.py`, the `user_id` is hardcoded to `1` when creating a blog. This needs to be dynamic based on the authenticated user.
