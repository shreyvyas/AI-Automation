import requests

response = requests.get("https://jsonplaceholder.typicode.com/users/1")

#print(response.status_code)

print(response.text)

#print(response.json())

#print(response["id"].json())

#data = response.json()

#print(data["id"])

