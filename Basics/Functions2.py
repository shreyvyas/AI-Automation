def greet():
    print("Hello World")

greet()


def greet1(name):
    print(name)

greet1("Shrey")

def calc(a, b):
    return a+b

result1 = calc(2,3)
print(result1)


def evenOdd(list1):
    for n in list1:
        if n%2==0:
            print("Even Number")
        else:
            print("Odd Number")

mylist = [1,2,3,4,5,6]
evenOdd(mylist)




add = lambda a, b : a + b
print(add(2,3))

multi = lambda a,b : a*b
print(multi(2,3))


mylist1 = [10,20,30,40]
result3 = list(filter(lambda x : x%3==0, mylist1))
print(result3)

result4 = list(map(lambda x : x*2, mylist1))
print(result4)


mylist2 = [1,2,3,4,2,4,5,3,5,5]
result5 = [x*2 for x in mylist2]
print(result5) 


