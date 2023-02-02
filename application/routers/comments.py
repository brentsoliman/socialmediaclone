from fastapi import FastAPI, APIRouter, status, HTTPException,Depends
from httpx import post
from sqlalchemy.orm import Session
from typing import List
from .. import schemas, models, oauth2
from ..database import get_db

router = APIRouter(
    tags=["Comment"]
)

@router.get("/posts/{post_id}/comments", response_model=List[schemas.CommentResponse])
def getting_all_comments_of_post(post_id: int, db: Session = Depends(get_db)):

    queried_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not queried_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post does not exist")
    
    queried_comment = db.query(models.Comment).filter(models.Comment.post_id == post_id).all()

    if not queried_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="There is no comments for this post")

    return queried_comment



#making a comment on a post
@router.post("/posts/{post_id}/comments")
def make_comment(comment: schemas.Comment,post_id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):

    commenter = db.query(models.User).filter(models.User.username == current_user.username).first()

    queried_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not queried_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
            detail="Post does not exist")

    new_comment = models.Comment(**comment.dict(), owner_id = commenter.id, post_id = post_id)
    
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)

    return new_comment