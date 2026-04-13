data = {"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

print(data["menu"])

print(data["menu"]["id"])

print(data["menu"]["popup"]["menuitem"])

print(data["menu"]["popup"]["menuitem"][0])