from pydantic import BaseModel
from datetime import datetime

from sqlalchemy import true

#Request data validation
class User(BaseModel):
    username: str

class Login(BaseModel):
    username: str
    password: str

class Post(BaseModel):
    content: str

class Comment(BaseModel):
    content: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: str

#Response data validation
class UserResponse(User):
    id: int
    class Config:
        orm_mode = True

class PostResponse(Post):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class CommentResponse(Comment):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True