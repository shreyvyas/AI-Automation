import requests
from utils_api.api_client import APIClient

client = APIClient()

def test_get_user():
    response = requests.get("https://reqres.in/api/users?page=2")
    print(response.json())
    print(response.status_code)
    print(response.headers)

def test_get_user1():
    response = client.get("/users?page=2")
    assert response.status_code == 200