from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from sqlalchemy.orm import Session
from src.database import get_db
from src.models.user import UserModel

# Secret key and algorithm for JWT
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

# OAuth2 dependency
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: int = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Invalid token")
        user = db.query(UserModel).filter(UserModel.id == user_id).first()
        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except :
        raise HTTPException(status_code=401, detail="Could not validate credentials")
