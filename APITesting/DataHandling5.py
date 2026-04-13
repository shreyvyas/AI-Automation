import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "title": "test",
    "body": "learning API with shrey",
    "userId": 27
}

response = requests.post(url, json=payload)

print(response.status_code)

data = response.json()

print(data)

try:
    assert data["body"] == "learning API with max", "body mismatch"
except Exception as e:
    print(e)