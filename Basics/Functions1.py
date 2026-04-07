def greet():
    print("Hello World")


greet()


def greet(name):
    print(name)


greet("shrey")


def cal(a, b):
    return a + b

result = cal(27,25)
print(result)


add = lambda a,b : a + b
print(add(2,3))

sub = lambda a,b : a - b
print(sub(2,3))

multi = lambda a, b : a * b
print(multi(2,3))