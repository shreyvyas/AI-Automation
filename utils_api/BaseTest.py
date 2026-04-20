import requests

import requests

class Utility:

    BASE_URL = "https://reqres.in/api/test-suite/collections"

    def __init__(self, endpoint):
        self.endpoint = endpoint

    def getRequest(self):
        return requests.get(f"{self.BASE_URL}{self.endpoint}")




#def test_sendrequest():

 #   response = requests.get("https://reqres.in/api/test-suite/collections/users/records")

  #  #print(response.json())
   # print(response.status_code) 


