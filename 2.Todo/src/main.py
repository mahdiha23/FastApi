from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.routers import todo_router  
from  src.database import engine, Base


Base.metadata.create_all(bind=engine)



@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Server is starting")
    yield
    print("Server is shutting down")

app = FastAPI(
    title="Todo Service",
    version="1",
    description="A web service for managing todo items with SQL DB",
    lifespan=lifespan,
)


app.include_router(todo_router)