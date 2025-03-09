# FastAPI Project

This is a structured FastAPI project designed for managing books and their associated data. The project is organized to promote clean architecture and scalability.

---

## Project Structure

### Root Directory

- **`.env`**: Environment variables file used to store sensitive configuration such as database URLs, API keys, etc.
- **`requirements.txt`**: Contains a list of all Python dependencies for the project.
- **`run.py`**: Entry point to start the FastAPI application.
- **`README.md`**: Documentation file explaining the project structure and usage.

---

### `/src/`

The core application logic is housed here.

#### `/src/books/`

This folder contains all modules related to the "books" feature.

- **`__init__.py`**: Makes the folder a Python package.
- **`book_data.py`**: Contains mock data or seed data for books (can be used for testing or initialization).
- **`models.py`**: Defines the database models (ORM classes) for books.
- **`routes.py`**: Contains the API endpoints (routes) for book-related operations.
- **`schemas.py`**: Defines the data validation and serialization schemas using Pydantic.
- **`service.py`**: Contains the business logic or service layer for books.

#### `/src/db/`

This folder handles database configurations and interactions.

- **`__init__.py`**: Makes the folder a Python package.
- **`config.py`**: Handles the database connection setup and configurations (e.g., SQLAlchemy configuration).
- **`main.py`**: Contains database initialization logic (e.g., creating tables or connecting to the database).

#### `/src/migrations/`

This folder contains database migration scripts managed by Alembic.

- **`env.py`**: Environment configuration for Alembic.
- **`script.py.mako`**: Template for Alembic migration scripts.
- **`versions/`**: Folder containing individual migration scripts.

---

### `/env/`

This directory typically contains virtual environment files (if created locally). It is excluded from version control using `.gitignore`.

---

### `/__pycache__/`

Automatically generated Python bytecode files for performance optimization. These files can be ignored.

---

## Usage

### 1. **Create a Virtual Environment**

Create a virtual environment to isolate project dependencies:

```bash
python -m venv env
```

Activate the virtual environment:

- On Windows:

  ```bash
  .\env\Scripts\activate
  ```

- On macOS/Linux:
  ```bash
  source env/bin/activate
  ```

### 2. **Install Dependencies**

Install the required dependencies using `pip`:

```bash
pip install -r requirements.txt
```

### 3. **Set Up Environment Variables**

Create a `.env` file in the root directory and add your configuration variables:

```
DATABASE_URL=sqlite:///./test.db
```

### 4. **Run the Application**

Start the FastAPI server:

```bash
python run.py
```

The server will start at `http://127.0.0.1:8000`.

### 5. **API Documentation**

Visit `http://127.0.0.1:8000/docs` for the Swagger UI documentation or `http://127.0.0.1:8000/redoc` for the ReDoc documentation.

---

## Features

- **Books Management**:

  - API endpoints for CRUD operations on books.
  - Data validation using Pydantic schemas.
  - Clean separation of routes, models, and services.

- **Database**:
  - Configurable database setup using `config.py`.
  - Compatible with SQLAlchemy or any other ORM.
  - Database migrations managed by Alembic.

---

## Folder Highlights

- **Separation of Concerns**: The project structure adheres to a modular approach, separating concerns like routing, models, schemas, and services.
- **Scalability**: The structure is designed to be scalable, making it easy to add new features or modules in the future.

---

## Alembic for Database Migrations

Alembic is used for handling database migrations. Below are some common commands:

### 1. **Initialize Alembic**

If you haven't already initialized Alembic, you can do so with:

```bash
alembic init -t async migrations
```

### 2. **Create a New Migration**

To create a new migration script after making changes to your models:

```bash
alembic revision --autogenerate -m "Description of changes"
```

### 3. **Apply Migrations**

To apply the migrations to the database:

```bash
alembic upgrade head
```

### 4. **Downgrade Migrations**

To revert the last migration:

```bash
alembic downgrade -1
```

### 5. **Check Current Migration**

To check the current migration version:

```bash
alembic current
```

---

## Contribution

1. Fork the repository.
2. Create a new branch for your feature: `git checkout -b feature-name`.
3. Commit your changes: `git commit -m "Add new feature"`.
4. Push to the branch: `git push origin feature-name`.
5. Submit a pull request.

---

##

you have any questions or issues, feel free to raise an issue in the repository. Happy coding! 🚀
