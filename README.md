# Todo API with Authentication

A RESTful Todo API built with Flask, MySQL, and SQLAlchemy, featuring user authentication.

## Features
- User signup and login
- Create, read, update, and delete todos
- MySQL database integration using SQLAlchemy ORM
- Environment variables for secure configuration

## Tech Stack
- Python, Flask
- MySQL, SQLAlchemy
- Postman (for testing)

## API Endpoints
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | /signup | Register a new user |
| POST | /login | Login existing user |
| GET | /todos | Get all todos |
| POST | /todos | Create a new todo |
| PUT | /todos/<id> | Update a todo |
| DELETE | /todos/<id> | Delete a todo |

## Setup
1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Create a `.env` file with your `DB_PASSWORD`
4. Run: `python todo_app.py`