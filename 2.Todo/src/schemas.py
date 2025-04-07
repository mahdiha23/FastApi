from pydantic import BaseModel, Field
from typing import Optional
from src.models import Priority 



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

