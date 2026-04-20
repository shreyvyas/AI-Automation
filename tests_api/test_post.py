import pytest
import requests
import json
from utils_api.api_client import APIClient

client = APIClient()

def test_create_user():

    with open(r"D:\AI-Automation\PythonWorkspace\data_api\user.json") as file:
        payload = json.load(file)

    response = client.post("/users", payload)

    #print(response.json())

    print(response.status_code)