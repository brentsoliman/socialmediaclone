from fastapi import FastAPI,Depends,status,HTTPException
from sqlalchemy.orm import Session
from .database import engine, get_db
from . import models,schemas
from .routers import users, posts, auth, comments


models.Base.metadata.create_all(bind = engine)

app = FastAPI(openapi_prefix="/api")

@app.get("/")
def index():
    return {"data": "this is the index"}


app.include_router(users.router)
app.include_router(posts.router)
app.include_router(auth.router)
app.include_router(comments.router)

