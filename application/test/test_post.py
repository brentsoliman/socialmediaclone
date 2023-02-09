from fastapi.testclient import TestClient
from ..app import app,get_db
from .. import utils, schemas
from .login_token import token


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from ..database import Base





#edited this one this is a bruteforce approach
#docker: postgresql://postgres:password123@172.17.0.3:5432/infoBrent
#normal: postgresql://postgres:password123@localhost/infoBrent

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@localhost:5003/postgres"


engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)





#testing getting a post
def test_get_post():
    response = client.get(
        "/users/test/posts",
        headers ={"Authorization":f"Bearer {token}"} 
    )


    test_string = ["tester post 1", "tester post 2"]


        

    assert response.status_code == 200

    for x in range(len(response.json())):
        assert schemas.PostResponse(**response.json()[x]).content == test_string[x]

#testing making a post
#def test_post_
    