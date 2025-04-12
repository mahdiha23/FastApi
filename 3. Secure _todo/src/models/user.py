from sqlalchemy import Column, Integer, String
from src.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=True)  # Optional field for email

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username}, email={self.email})>"
