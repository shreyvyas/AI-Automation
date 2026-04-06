s1 = "Shrey"
print("This is " +s1)
print(type(s1))

print(s1[0])

s2 = "bold"

#replace b with g

#s2[0] = 'g'                             does not support item assignment
#print(s2)

s2 = 'g' + s2[1:]
print(s2)

s3 = "strinks"
s3 = s3[0:5] + "g" + s3[-1];
print(s3)

s3 = s3.split(" ");
print(s3)

s4 = "This is Python Programming"
#s4 = s4.split()
print(s4)
print(type(s4))

print('T' in s4);

print(s4.index('T'));

print(len(s4))

print(s4.find("This"))
print(s4.find("is"))
print(s4.find("Python"))
print(s4.find("Programming"))

print(s4.count("i"))

words = ["Hello", "World"]

result = " ".join(words)

print(result)


letter = "This"
newLetter = " ".join(letter)
print(newLetter)