from sqlalchemy import Column, Integer, String, Boolean, Enum
from src.database import Base
from enum import IntEnum

class Priority(IntEnum):
    LOW = 3
    MEDIUM = 2
    HIGH = 1

class TodoModel(Base):
    __tablename__ = "todos"
    todo_id = Column(Integer, primary_key=True, index=True)
    todo_name = Column(String, nullable=False)
    done = Column(Boolean, default=False)
    priority = Column(Enum(Priority), default=Priority.LOW)
