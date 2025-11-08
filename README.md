Todo API Documentation

Base URL: http://127.0.0.1:8000/

This is a simple Todo API built with FastAPI, SQLite, and SQLAlchemy. It allows users to manage todos with the ability to create, read, update, delete, and sort todos.

Table of Contents

Installation

Start the API

Root Route

Get All Todos

Create Todo

Mark Todo as Done

Delete All Todos

Delete Single Todo

Data Validation

Example cURL Requests

Installation

Make sure you have Python 3.12+ installed.

Install dependencies:

pip install fastapi uvicorn sqlalchemy


Your project structure should look like:

py-sql-todo/
│
├── main.py
├── database.py
└── models.py

Start the API

From your project folder:

python -m uvicorn main:app --reload


The --reload flag automatically reloads the server on code changes.

Open your browser to access the API:

http://127.0.0.1:8000/


For interactive testing and docs:

http://127.0.0.1:8000/docs

Root Route

GET /

Response:

{
  "message": "Todo API is running!"
}

Get All Todos

GET /todos/

Query Parameters:

Parameter	Type	Default	Description
sort	string	recent	recent = sort by creation date (default), time = sort by due date

Response Example:

[
  {
    "id": 1,
    "title": "Buy groceries",
    "description": "Milk, eggs, bread",
    "done": false,
    "created_at": "2025-11-08T12:00:00",
    "due_date": "2025-11-10T17:00:00"
  }
]

Create Todo

POST /todos/

Request Body (JSON):

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "due_date": "2025-11-10T17:00:00"
}


title (string, required)

description (string, optional)

due_date (datetime, optional, ISO 8601 format: YYYY-MM-DDTHH:MM:SS)

Response Example:

{
  "id": 1,
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "done": false,
  "created_at": "2025-11-08T12:00:00",
  "due_date": "2025-11-10T17:00:00"
}


Validation Error Example:

{
  "detail": [
    {
      "loc": ["body", "due_date"],
      "msg": "invalid datetime format",
      "type": "value_error.datetime"
    }
  ]
}

Mark Todo as Done

PUT /todos/{todo_id}/done

Path Parameters:

Parameter	Type	Description
todo_id	int	ID of the todo

Response Example:

{
  "message": "Todo marked as done"
}


Error Example (if todo not found):

{
  "detail": "Todo not found"
}

Delete All Todos

DELETE /todos/

Response Example:

{
  "message": "All todos deleted"
}

Delete Single Todo

DELETE /todos/{todo_id}

Path Parameters:

Parameter	Type	Description
todo_id	int	ID of the todo

Response Example:

{
  "message": "Todo deleted"
}


Error Example (if todo not found):

{
  "detail": "Todo not found"
}

Data Validation

due_date must be in ISO 8601 format:

YYYY-MM-DDTHH:MM:SS


Invalid inputs return clear messages indicating which field is incorrect.

Example: "tomorrow 5 pm" will return:

{
  "detail": [
    {
      "loc": ["body", "due_date"],
      "msg": "invalid datetime format",
      "type": "value_error.datetime"
    }
  ]
}

Example cURL Requests

Get all todos (recent by default):

curl -X GET "http://127.0.0.1:8000/todos/"


Get all todos (sorted by due date):

curl -X GET "http://127.0.0.1:8000/todos/?sort=time"


Create a todo:

curl -X POST "http://127.0.0.1:8000/todos/" \
-H "Content-Type: application/json" \
-d '{"title":"Buy groceries","description":"Milk, eggs, bread","due_date":"2025-11-10T17:00:00"}'


Mark todo as done (id=1):

curl -X PUT "http://127.0.0.1:8000/todos/1/done"


Delete all todos:

curl -X DELETE "http://127.0.0.1:8000/todos/"


Delete single todo (id=1):

curl -X DELETE "http://127.0.0.1:8000/todos/1"


Swagger UI:
For interactive testing and examples, open:

http://127.0.0.1:8000/docs