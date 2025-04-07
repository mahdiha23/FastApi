# Todo Application

A simple FastAPI-based web service for managing a todo list. This application supports the following functionalities:

- **CRUD operations**: Create, Read, Update, and Delete todos.
- **SQLite storage**: Todos are stored in a SQLite database for persistence.
- **Validation**: Request and response validation using Pydantic models.
- **Priority levels**: Enums for LOW, MEDIUM, and HIGH priorities.

## Features

- Retrieve all todos or a specific todo by ID.
- Add new todos with customizable priorities and statuses.
- Update existing todos (supports partial updates).
- Delete todos by ID.
- Persist data using SQLite.
- Error handling for invalid operations or data.

## Project Highlights

- Uses **SQLAlchemy** for database modeling and interaction.
- Implements **modular design** for scalability with separate files for models, schemas, database, and routers.
- Provides a clean and easy-to-use RESTful API.
