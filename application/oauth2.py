from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from typing import Union
from datetime import datetime, timedelta
from . import schemas, models
from .database import get_db

SECRET_KEY = "fb03b58a1fec2b0727936406dac7c766f3d71114c1e11982dd608fbe6ff0264a"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

oauth2_scheme =  OAuth2PasswordBearer(tokenUrl = "login")

def create_access_token(data: dict, expired_data: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expired_data:
        expire = datetime.utcnow() + expired_data
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})

    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    return encoded_jwt

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credentials_exception

    user = db.query(models.User).filter(models.User.username == username).first()

    if not user:
        raise credentials_exception

    return user
    