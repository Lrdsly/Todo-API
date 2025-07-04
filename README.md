# Todo API Project

## Description
This is a simple Todo List API built with Django and Django REST Framework. It allows users to create, read, update, and delete todo items with features like status tracking (Doing, Done, Expired) and deadlines.

## Features
- Add and manage todo items
- Filter by status and deadline
- RESTful endpoints for CRUD operations

## Endpoints
- `GET /todos/` - List all todos
- `POST /todos/` - Create a new todo
- `GET /todos/<id>/` - Get a specific todo
- `PUT /todos/<id>/` - Update a todo
- `DELETE /todos/<id>/` - Delete a todo

## Tech Stack
- Python
- Django
- Django REST Framework

## Setup
1. Clone the repo: `git clone https://github.com/lrdsly/Todo-API.git`
2. Install dependencies: `pip install -r requirements.txt`
3. Run migrations: `python manage.py migrate`
4. Start the server: `python manage.py runserver`

## Future Improvements
- Add search functionality
- Implement notifications

