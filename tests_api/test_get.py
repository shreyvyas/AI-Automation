from utils_api.BaseTest import Utility
import requests

client = Utility("/users/records")

def test_getrequest():
    
    response = client.getRequest()

    response.status_code