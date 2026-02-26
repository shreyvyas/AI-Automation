myDict = {

    "name" : "shrey",
    "age" : 36,
    "city" : "bengaluru"

}

for key in myDict:
    print(key, myDict[key])


print(myDict["name"])
print(myDict["age"])
print(myDict["city"])

print(myDict.keys())
print(myDict.values())

myDict["company"] = "candescent"
print(myDict)

myDict.pop("company")
print(myDict)