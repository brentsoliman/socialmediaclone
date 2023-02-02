from fastapi.testclient import TestClient
from ..app import app
from .. import utils, schemas
from .login_token import token

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
def test_post_
    