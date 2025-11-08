from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import Optional
from datetime import datetime
from database import Base, engine, SessionLocal
from models import Todo
from pydantic import BaseModel, Field

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Todo API")

class TodoCreate(BaseModel):
    title: str = Field(..., example="Buy groceries")
    description: Optional[str] = Field(None, example="Milk, eggs, bread")
    due_date: Optional[datetime] = Field(
        None,
        example="2025-11-10T17:00:00",
        description="Must be in ISO 8601 format: YYYY-MM-DDTHH:MM:SS"
    )

class TodoResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    done: bool
    created_at: datetime
    due_date: Optional[datetime]

    class Config:
        orm_mode = True

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Todo API is running!"}

@app.get("/todos/", response_model=list[TodoResponse])
def get_todos(sort: Optional[str] = "recent", db: Session = Depends(get_db)):
    if sort == "time":
        todos = db.query(Todo).order_by(Todo.due_date.asc()).all()
    else:
        todos = db.query(Todo).order_by(Todo.created_at.desc()).all()
    return todos

@app.post("/todos/", response_model=TodoResponse)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db)):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        due_date=todo.due_date
    )
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

@app.put("/todos/{todo_id}/done")
def mark_done(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    todo.done = True
    db.commit()
    return {"message": "Todo marked as done"}

@app.delete("/todos/")
def delete_all_todos(db: Session = Depends(get_db)):
    db.query(Todo).delete()
    db.commit()
    return {"message": "All todos deleted"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return {"message": "Todo deleted"}
