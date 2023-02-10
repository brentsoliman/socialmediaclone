from fastapi.testclient import TestClient
from ..app import app,get_db
from .. import utils, schemas
from .login_token import token
from .database_test import override_get_db




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
def test_making_post():
    response = client.post(
        "/users/posts",
        json = {
            "content":"this the content made by the tester program"
        },
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 200


#testing updaating the post
def test_update_post():
    response = client.put(
        "/posts/3",
        json ={
            "content":"this is the update post from the test program"
        },
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 200

def test_delete_post():
    response = client.delete(
        "/posts/3",
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 204