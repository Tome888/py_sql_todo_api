# Todo API

A simple Todo API built with FastAPI, SQLite, and SQLAlchemy. You can create, read, update, delete, and sort your todos.

## Base URL: http://127.0.0.1:8000/

## Run API: docker-compose up --build

- Go to `http://127.0.0.1:8000/` to see it running.
- Check interactive/Swagger docs at `http://127.0.0.1:8000/docs`.

## Endpoints

### Get all todos

**GET** `/todos/`

Optional query parameters:

- `?sort=recent` (default)
- `?sort=time` (by due date)

### Create a todo

**POST** `/todos/`

#### Request body:

```json
{
  "detail": [
    {
      "loc": ["body", "due_date"],
      "msg": "invalid datetime format",
      "type": "value_error.datetime"
    }
  ]
}
```

## Notes

### Invalid `due_date` format

If the `due_date` is invalid, you will receive a clear error message like this:

```json
{
  "detail": [
    {
      "loc": ["body", "due_date"],
      "msg": "invalid datetime format",
      "type": "value_error.datetime"
    }
  ]
}
```

## Sorting

- `recent` = newest first
- `time` = soonest due first

# cURL

### Get todos

curl -X GET "http://127.0.0.1:8000/todos/"

### Create todo

curl -X POST "http://127.0.0.1:8000/todos/" \
-H "Content-Type: application/json" \
-d '{"title":"Buy groceries","description":"Milk, eggs","due_date":"2025-11-10T17:00:00"}'

### Mark done

curl -X PUT "http://127.0.0.1:8000/todos/1/done"

### Delete single

curl -X DELETE "http://127.0.0.1:8000/todos/1"

### Delete all

curl -X DELETE "http://127.0.0.1:8000/todos/"
