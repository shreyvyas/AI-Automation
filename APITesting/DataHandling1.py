data = {
    "id": 1,
    "name": "Shrey",
    "skills": ["Python", "API", "Selenium"],
    "address": {
        "city": "Mumbai",
        "pincode": 400001
    }
}

#print all the skills
print(data["skills"])

#print first skill
print(data["skills"][0])

#print city name
print(data["address"]["city"])

#print pin code
print(data["address"]["pincode"])