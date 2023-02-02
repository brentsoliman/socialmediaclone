from datetime import timedelta
from typing import List
from fastapi import FastAPI,Depends,status,HTTPException,APIRouter
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models, schemas,utils, oauth2
from ..database import get_db


router = APIRouter(
    tags=["Register and Login"]
)

@router.post("/register")
def register(user: schemas.Login, db: Session = Depends(get_db)):
    finding_user = db.query(models.User).filter(models.User.username == user.username).first()

    if finding_user is not None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already taken")
    
    user.password = utils.get_password_hash(user.password)
    
    new_user = models.User(**user.dict())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

@router.post("/login")
def login(user: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    queried_user = db.query(models.User).filter(models.User.username == user.username).first()

    if not queried_user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")

    #boolean for verification if the user logging in is that user
    isUser = utils.verify_password(user.password,queried_user.password)

    if not isUser:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Wrong password")
    
    token_expiry = oauth2.ACCESS_TOKEN_EXPIRE_MINUTES

    token = oauth2.create_access_token({"sub":queried_user.username},timedelta(minutes=token_expiry))

    return {"access_token": token, "token_type":"bearer"}