from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from datetime import timedelta
from src.database import get_db
from src.models.user import UserModel
from src.schemas.auth import Token ,UserCreate
from src.utils.jwt import create_access_token
from passlib.context import CryptContext
from src.database import Base, engine


auth_router = APIRouter()
Base.metadata.create_all(bind=engine)
# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# SECRET_KEY = "your_secret_key"  # Replace with your secret key or use environment variables
ACCESS_TOKEN_EXPIRE_MINUTES = 30  # Token expiration time

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(db: Session, username: str, password: str):
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if user and verify_password(password, user.password):
        return user
    return None

@auth_router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

@auth_router.post("/register", status_code=201)
def register(user: UserCreate, db: Session = Depends(get_db)):
    # Check if the username already exists
    existing_user = db.query(UserModel).filter(UserModel.username == user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")

    # Hash the password and create a new user
    hashed_password = hash_password(user.password)
    new_user = UserModel(username=user.username, password=hashed_password, email=user.email)
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return {"message": "User registered successfully", "user": {"username": new_user.username, "email": new_user.email}}