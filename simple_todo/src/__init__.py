from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from typing import List, Optional
from enum import IntEnum
from pydantic import BaseModel, Field




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting")
    yield
    print("Server is shutting down")


app = FastAPI(
    title="Todo Service",
    version="0.1",
    description="A simple web service for managing todo items",
    lifespan=lifespan,
)


class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoBase(BaseModel):
    todo_name: str = Field(..., min_length=3, max_length=32, description="Name of the todo")
    done: bool = Field(..., description="Status of the todo")
    priority: Priority = Field(default=Priority.LOW, description="Priority of the todo")

class TodoCreate(TodoBase):
    pass

class Todo(TodoBase):
    todo_id: int = Field(..., description="Unique identifier of the todo")

class TodoUpdate(BaseModel):
    todo_name: Optional[str] = Field(None, min_length=3, max_length=32, description="Name of the todo")
    done: Optional[bool] = Field(None, description="Status of the todo")
    priority: Optional[Priority] = Field(None, description="Priority of the todo")
    
    
    
    

all_todos = [
    {"todo_id": 1, "todo_name": "Amir", "done": False, "priority": Priority.LOW},
    {"todo_id": 2, "todo_name": "Mohammad", "done": False, "priority": Priority.HIGH},
    {"todo_id": 3, "todo_name": "Mahdi", "done": True, "priority": Priority.LOW},
    {"todo_id": 4, "todo_name": "Ghasem", "done": False, "priority": Priority.MEDIUM},
]



@app.get("/todos", response_model=List[Todo])
def get_todos():
    return [Todo(**todo) for todo in all_todos]  # Ensures items match the Todo model



@app.get("/todos/{todo_id}", response_model=Todo)
def get_todo(todo_id: int):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            return Todo(**todo)
    raise HTTPException(status_code=404, detail="Todo not found")


@app.post("/todos", response_model=Todo)
def create_todo(todo: TodoCreate):
    new_todo_id = max(todo["todo_id"] for todo in all_todos) + 1 if all_todos else 1
    new_todo = {
        "todo_id": new_todo_id,
        "todo_name": todo.todo_name,
        "done": todo.done,
        "priority": todo.priority,
    }
    all_todos.append(new_todo)
    return Todo(**new_todo)


@app.put("/todos/{todo_id}", response_model=Todo)
def update_todo(todo_id: int, updated_todo: TodoUpdate):
    for todo in all_todos:
        if todo["todo_id"] == todo_id:
            if updated_todo.todo_name is not None:
                todo["todo_name"] = updated_todo.todo_name
            if updated_todo.done is not None:
                todo["done"] = updated_todo.done
            if updated_todo.priority is not None:
                todo["priority"] = updated_todo.priority
            return Todo(**todo)
    raise HTTPException(status_code=404, detail="Todo not found")


@app.delete("/todos/{todo_id}", response_model=Todo)
def delete_todo(todo_id: int):
    for index, todo in enumerate(all_todos):
        if todo["todo_id"] == todo_id:
            deleted_todo = all_todos.pop(index)
            return Todo(**deleted_todo)
    raise HTTPException(status_code=404, detail="Todo not found")
