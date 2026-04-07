num = [10,20,30,40]

for i in range(len(num)):
    print(num[i])


for i in range(len(num)):
    print(i, num[i])

for i, val in enumerate(num):
    print(i, val)


for i in enumerate(num):
    print(i)