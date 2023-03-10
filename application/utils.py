from typing import Union
from passlib.context import CryptContext
from fastapi import Depends, status, HTTPException
from sqlalchemy.orm import Session
from . import models
from .database import get_db



pwd_context = CryptContext(schemes=["bcrypt"], deprecated = "auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def isExist_user(username: Union [str, None], db: Session = Depends(get_db)):
    if not username:
        queried_user = None
    else:
        queried_user = db.query(models.User).filter(models.User.username == username)
        

    if not queried_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")

    return queried_user

def isExist_post(id: int,  db: Session = Depends(get_db)):
    queried_post = db.query(models.Post).filter(models.Post.id == id)

    if not queried_post.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post does not exist")
        
    return queried_post

def isExist_comment(id: int, db: Session = Depends(get_db)):
    queried_comment = db.query(models.Comment).filter(models.Comment.id == id)

    if not queried_comment.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Comment does not exist")

    return queried_comment

#adding a function to get id based on username

def get_username(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    queried_user = isExist_user(user.first().username, db)

    return queried_user.first().username

def isUser(id: int, username: str, db: Session = Depends(get_db)):
    username_of_id = get_username(id, db)

    if username_of_id == username:
        return True
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN)

    
