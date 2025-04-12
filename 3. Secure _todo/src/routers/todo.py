from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.todo import TodoModel
from src.models.user import UserModel
from src.schemas.todo import Todo, TodoCreate, TodoUpdate
from src.authen.auth import get_current_user

todo_router = APIRouter()

@todo_router.get("/todos", response_model=list[Todo])
def get_todos(db: Session = Depends(get_db)):
    todos = db.query(TodoModel).all()
    return [Todo(**todo.__dict__) for todo in todos]

@todo_router.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    return Todo(**todo.__dict__)

@todo_router.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate, db: Session = Depends(get_db) ,
                    current_user: UserModel = Depends(get_current_user),):
    new_todo = TodoModel(**todo.dict())
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return Todo(**new_todo.__dict__)


@todo_router.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate, db: Session = Depends(get_db)
                , current_user: UserModel = Depends(get_current_user)):
    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    for key, value in updated_todo.dict(exclude_unset=True).items():
        setattr(todo, key, value)
    db.commit()
    db.refresh(todo)
    return Todo(**todo.__dict__)

@todo_router.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int, db: Session = Depends(get_db)
                    , current_user: UserModel = Depends(get_current_user)):

    todo = db.query(TodoModel).filter(TodoModel.todo_id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail="Todo not found")
    db.delete(todo)
    db.commit()
    return Todo(**todo.__dict__)
