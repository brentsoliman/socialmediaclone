from fastapi.testclient import TestClient
from .. import schemas
from ..app import app,get_db
from .. import utils, schemas
from .login_token import token
from .database_test import override_get_db




app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


def test_get_post_comment():
    response = client.get(
        "/posts/2/comments",
        headers ={"Authorization":f"Bearer {token}"} 
    )


    test_string = ["brent's another comment","neil's this comment","neil's that comment"]

    assert response.status_code == 200

    for x in range(len(response.json())):
        print(x)
        print("json size: ", len(response.json()))
        assert schemas.CommentResponse(**response.json()[x]).content == test_string[x]

def test_make_comment():
    response = client.post(
        "/posts/1/comments",
        json={
            "content":"this comment was from test"
        },
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 200

def test_update_comment():
    response = client.put(
        "/comments/4",
        json={
            "content":"edited comment from test"
        },
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 200

def test_delete_comment():
    response = client.delete(
        "/comments/4",
        headers ={"Authorization":f"Bearer {token}"}
    )

    assert response.status_code == 204

