from fastapi import FastAPI,Depends,status,HTTPException,APIRouter, Response
from sqlalchemy.orm import Session
from typing import List
from .. import models,schemas,oauth2, utils
from ..database import get_db

router = APIRouter(
    tags=["User"]
)

#getting all the users in the database
@router.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db),current_user: schemas.User = Depends(oauth2.get_current_user)):
    if current_user.username != "dev":
        print(current_user.username)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    all_users = db.query(models.User).all()
    return all_users

#registering an account


#getting a specific user
@router.get("/users/{username}",response_model=schemas.UserResponse)
def getting_one_user(username: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    queried_user = db.query(models.User).filter(models.User.username == username).first()

    if not queried_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")

    return queried_user

#deleting an user
#still testing this one
@router.delete("/users/{username}")
def delete_user(username: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    queried_user = utils.isExist_user(username,db)

    queried_user.delete()


    return Response(status_code=status.HTTP_204_NO_CONTENT)

