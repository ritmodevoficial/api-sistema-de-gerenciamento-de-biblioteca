# Library Management System

This is a simple API for a library management system built using FastAPI and SQLAlchemy.

## Features

- Create and manage books
- Create and manage students
- Handle borrowing and returning of books

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/bugramatik/library-management-api.git
    ```

2. Navigate to the directory:

    ```bash
    cd library-management-api
    ```

3. (Optional) Create a virtual environment:

    ```bash
    python -m venv venv
    ```

    And activate it:

    - On Unix or MacOS:

        ```bash
        source venv/bin/activate
        ```

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

4. Install the requirements:

    ```bash
    pip install -r requirements.txt
    ```

5. Create a Postgres database for the application:

    ```sql
    CREATE DATABASE lmsdb;
    ```
6. Restore the database from dumpfile
   ```bash
   psql -U postgres -d lmsdb < dumpfile.sql
   ```
7. Update the database connection settings in `database/__init__.py` according to your PostgreSQL setup.


## Usage

Run the application:

```bash
uvicorn main:app --reload
```
This will start the application on http://127.0.0.1:8000. You can explore the API via the built-in Swagger UI at http://127.0.0.1:8000/docs.

## Endpoints

http://localhost:8000/docs#/ - Swagger UI can be investiaged for the endpoints.

