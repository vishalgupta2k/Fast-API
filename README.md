<!-- LOGO SECTION -->
<p align="center">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI Logo" width="120"/>
  <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="PostgreSQL Logo" width="90"/>
  <img src="https://avatars.githubusercontent.com/u/59588641?s=200&v=4" alt="SQLModel Logo" width="90"/>
</p>

<h1 align="center">📚 Fast-API Book & User Management</h1>
<p align="center">
  <b>A modern, async-ready RESTful API for managing books and users.</b><br>
  <i>Built with FastAPI, SQLModel, and PostgreSQL.</i>
</p>

<p align="center">
  <a href="https://github.com/your-username/fast-api-book-user/pulls">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square" alt="PRs Welcome"/>
  </a>
  <a href="https://github.com/your-username/fast-api-book-user/issues">
    <img src="https://img.shields.io/github/issues/your-username/fast-api-book-user?style=flat-square" alt="Issues"/>
  </a>
  <img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat-square" alt="License"/>
</p>

---

# 🚀 Features

- **User Registration & Authentication**
  - Secure password hashing
  - JWT-based login
- **Book Management**
  - CRUD operations for books
  - Async database access
- **Environment-based Configuration**
- **Automatic Database Migrations**
- **Clean, Modular Code Structure**

---

## 🛠️ Tech Stack

<p align="left">
  <img src="https://fastapi.tiangolo.com/img/logo-margin/logo-teal.png" alt="FastAPI" width="50" title="FastAPI"/>
  <img src="https://avatars.githubusercontent.com/u/59588641?s=200&v=4" alt="SQLModel" width="50" title="SQLModel"/>
  <img src="https://www.postgresql.org/media/img/about/press/elephant.png" alt="PostgreSQL" width="50" title="PostgreSQL"/>
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/pydantic.svg" alt="Pydantic" width="50" title="Pydantic"/>
  <img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/passlib.svg" alt="Passlib" width="50" title="Passlib"/>
  <img src="https://jwt.io/img/pic_logo.svg" alt="JWT" width="50" title="JWT"/>
</p>

- **FastAPI** - High-performance Python web framework
- **SQLModel** - ORM for SQL databases
- **PostgreSQL** - Relational database
- **Pydantic** - Data validation
- **Passlib** - Password hashing
- **JWT** - Authentication tokens

---

## ⚡ Quickstart

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/fast-api-book-user.git
   cd fast-api-book-user
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Create a `.env` file in the root directory:

   ```
   DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/yourdb
   SECRET_KEY=your_secret_key
   ALGORITHM=HS256
   ACCESS_TOKEN_EXPIRE_MINUTES=30
   ```

4. **Run the application**

   ```bash
   uvicorn src.__init__:app --reload
   ```

5. **API Docs**

   Visit [http://localhost:8000/docs](http://localhost:8000/docs) for interactive Swagger UI.

---

## 📖 API Endpoints

### User

- `POST /api/v1/user/` - Register a new user
- `POST /api/v1/user/login` - Login and get JWT token

### Books

- `GET /api/v1/books/` - List all books
- `GET /api/v1/books/{book_uid}` - Get book by UID
- `POST /api/v1/books/` - Add a new book
- `PUT /api/v1/books/{book_uid}` - Update a book
- `DELETE /api/v1/books/{book_uid}` - Delete a book

---

## 🧩 Project Structure

```
e:\Fast-API\
│
├── src\
│   ├── books\
│   ├── users\
│   ├── db\
│   └── config.py
├── .env
├── requirements.txt
└── README.md
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

- Fork the repo and create your branch from `main`.
- Ensure your code passes linting and tests.
- Open a PR with a clear description and link to any relevant issues.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](https://github.com/your-username/fast-api-book-user/pulls)

---

## 📝 License

MIT License

---

## 👤 Author

- [Vishal Gupta](https://github.com/vishalgupta2k)

---

> Built with ❤️ using FastAPI.
