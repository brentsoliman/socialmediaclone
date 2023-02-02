from fastapi.testclient import TestClient
from ..app import app
from .. import utils,schemas
from .login_token import token

client = TestClient(app)




def login_to_test():
    response  = client.post(
            "/login",
            data={
                "username":"dev",
                "password":"developer"
            }
    )

    return response

def test_get_user_id():
    response = client.get(
        "/users/test",
        headers ={"Authorization":f"Bearer {token}"} 
    )
    output = {
        "username":"test",
        "id":5
    }

    var = schemas.UserResponse(**response.json())

    assert response.status_code == 200
    assert var.username == "test"




