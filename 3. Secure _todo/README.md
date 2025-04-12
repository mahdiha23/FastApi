# Todo Application

A simple FastAPI-based web service for managing a todo list. This application supports the following functionalities:

- **CRUD operations**: Create, Read, Update, and Delete todos.
- **JWT Authentication**: Secure access to endpoints using JSON Web Tokens.
- **SQLite storage**: Todos are stored in a SQLite database for persistence.
- **Validation**: Request and response validation using Pydantic models.
- **Priority levels**: Enums for LOW, MEDIUM, and HIGH priorities.

## Features

- Retrieve all todos or a specific todo by ID (requires authentication).
- Add new todos with customizable priorities and statuses (requires authentication).
- Update existing todos (supports partial updates; requires authentication).
- Delete todos by ID (requires authentication).
- Persist data using SQLite.
- Error handling for invalid operations or data.
- Secure token-based authentication using FastAPI's dependency injection.

## Project Highlights

- Uses **SQLAlchemy** for database modeling and interaction.
- Implements **JWT authentication** for secure user login and protected endpoints.
- Implements **modular design** for scalability with separate files for models, schemas, database, routers, and authentication.
- Provides a clean and easy-to-use RESTful API.

## Authentication

This application uses **JSON Web Tokens (JWT)** to secure access to its endpoints. Authentication works as follows:

1. Users must log in using valid credentials to receive a token.
2. The token is included in the `Authorization` header (`Bearer <token>`) for protected routes.
3. Tokens are verified for validity and expiration before granting access.

---

Feel free to copy this and tweak it further to suit your needs! If you need help implementing or documenting other features, let me know.
