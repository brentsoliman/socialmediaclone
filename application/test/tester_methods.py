import requests


def give_token_test():
    data = {
    "username":"dev",
    "password":"developer"
    }

    url = "http://127.0.0.1:8000"
    response = requests.post(f"{url}/login",data = data)
    token = response.json().get("access_token")
    return token

def make_account_test():
    data = {
    "username":"tester",
    "password":"testaccount"
    }

    url = "http://127.0.0.1:8000"
    response = requests.post(f"{url}/register",data = data)
