with open("D:\AI-Automation\PythonWorkspace\FileRead\data.txt", "r") as file:
    content = file.read()
    print(content)


with open("D:\AI-Automation\PythonWorkspace\FileRead\data.txt", "r") as file1:
    content = file1.readlines()
    print(content)


with open("D:\AI-Automation\PythonWorkspace\FileRead\data.txt", "a") as file2:
      file2.write("\nNew Line Added using a")


with open("D:\AI-Automation\PythonWorkspace\FileRead\data.txt", "r") as file3:
    content = file3.readlines()
    print(content)