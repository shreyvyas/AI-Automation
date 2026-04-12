data = {
    "users": [
        {
            "id": 1,
            "name": "Shrey",
            "roles": ["admin", "user"]
        },
        {
            "id": 2,
            "name": "Ankit",
            "roles": ["user"]
        }
    ]
}

#Get name of first user
print(data["users"][0]["name"])

#Get second role of first user
print(data["users"][0]["roles"][1])

#Get name of second user
print(data["users"][1]["name"])