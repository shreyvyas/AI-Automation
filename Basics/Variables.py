a = 10                                         #integer
print("Integer: ", a)
print(type(a))                                  #to check the datatype of a variable

b = 20.1                                       #float
print("Float: ", b)
print(type(b))

str = "shrey"                                  #string
print(str)
print(type(str))

list = [1,2,3,"Shrey", 10.1]                   #list: mutable, ordered, mixed datatype, allows duplicates
print(list)
print(type(list))

tup = (1,2,3,4,5,6,"shrey")                   #tup: immutable, ordered
print(tup)
print(type(tup))

set1 = {10, True, 90.5, "shrey"}              #set: duplicates are not allowed, not ordered
print(set1)
print(type(set1))

dict1 = {"name":"shrey", "age": 36, "city":"bengaluru"}      #key-value pair, used in test automation
print(dict1.keys())
print(dict1.values())
print(type(dict1))

value = False
print(value)
