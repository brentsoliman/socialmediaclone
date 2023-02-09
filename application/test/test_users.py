from fastapi.testclient import TestClient
from ..app import app,get_db
from .. import utils,schemas
from .login_token import token
from .database_test import override_get_db




app.dependency_overrides[get_db] = override_get_db


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




