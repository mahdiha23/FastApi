import jwt
from datetime import datetime, timedelta

# Secret key for signing the JWT (store this in environment variables for better security)
SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"

def create_access_token(data: dict, expires_delta: timedelta = timedelta(minutes=30)):
    """
    Create a JWT access token.
    :param data: The payload to encode in the token (e.g., user details).
    :param expires_delta: The lifespan of the token.
    :return: Encoded JWT as a string.
    """
    to_encode = data.copy()
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
