from ast import In
from typing import Collection
from .database import Base
from sqlalchemy import Column, ForeignKey, Integer,String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False)
    username = Column(String,nullable=False, unique=True)
    password = Column(String, nullable=False)

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer,primary_key=True,nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=(text("now()")))

class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer,primary_key=True,nullable=False)
    content = Column(String, nullable=False)
    owner_id = Column(Integer,ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    post_id = Column(Integer,ForeignKey("posts.id", ondelete="CASCADE"), nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=(text("now()")))




