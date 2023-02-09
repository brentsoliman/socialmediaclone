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
        "/posts/7/comments",
        headers ={"Authorization":f"Bearer {token}"} 
    )


        test_string = ["brent's another commment","neil's this commment","neil's that commment"]

        assert response.status_code == 200

        for x in range(len(response.json())):
            assert schemas.CommentResponse(**response.json()[x]).content == test_string[x]