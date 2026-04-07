str = "shrey"

for s in str:
    print(s)


for s in str:
    print(s.upper())


num = [1,2,3,4,5,6]

for n in num:
    if(n % 2 == 0):
        print(n)

for n in num:
    if(n%2==0):
        print("Fizz")
    elif(n % 3== 0):
        print("Buzz")
    else:
        print("FizzBuzz")


users = {
    "name": "shrey",
    "age": 36,
    "city": "bengaluru" 
}

for key in users:
    print(key)

for value in users.values():
    print(value)

for key, value in users.items():
    print(key, value)

