from webbrowser import get
from fastapi import FastAPI,Depends,status,HTTPException,APIRouter, Response
from sqlalchemy.orm import Session
from typing import List
from .. import models,schemas,oauth2, utils
from ..database import get_db

router = APIRouter(
    tags=["Post"]
)

#getting a post
@router.get("/users/{username}/posts", response_model=List[schemas.PostResponse])
def get_post(username: str, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    queried_user = db.query(models.User).filter(models.User.username == username).first()

    if not queried_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")

    user_posts = db.query(models.Post).filter(models.Post.owner_id == queried_user.id).all()

    if not user_posts:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not have any post")
    
    return user_posts

#user making a post
@router.post("/users/posts")
def making_post(post: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    queried_user = db.query(models.User).filter(models.User.username == current_user.username).first()

    if not queried_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="User does not exist")

    new_post = models.Post(**post.dict(), owner_id = queried_user.id)

    db.add(new_post)
    db.commit()
    db.refresh(new_post)

    return new_post
    
#updating a post

@router.put("/posts/{post_id}")
def updating_post(post_id: int, post: schemas.Post, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    #editing this one

    queried_post = utils.isExist_post(post_id,db)


    #edit this one if should we use the id than the username
    post_username = utils.get_username(queried_post.first().owner_id,db)
    if (current_user.username == post_username):
        queried_post.update(post.dict(), synchronize_session=False)
        db.commit()
    else:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,
            detail="You must be the poster in order to edit it")


    return queried_post.first()

@router.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    
    
    queried_post = utils.isExist_post(post_id, db)


    userExist = utils.isUser(queried_post.first().owner_id, current_user.username, db)

    if userExist:
        queried_post.delete(synchronize_session=False)
        db.commit()
    else:
        raise Exception(status_code=status.HTTP_403_FORBIDDEN,
        detail="You can only delete your own post")



    return Response(status_code=status.HTTP_204_NO_CONTENT)
