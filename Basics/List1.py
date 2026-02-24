list1 = ["kohli", "rohit", "bumrah"]
print(list1)                                                         #print list


#indexing in list
print(list1[0])
print(list1[1])
print(list1[2])
#print(list1[3])                                                  index out of range


#add element
list1.append("arshdeep")                                          #add at last index
print(list1)

list1.insert(0, "siraj") 
print(list1)

list1[0] = "rana"
print(list1)


#remove element
list1.remove("bumrah")
print(list1)

list1.pop()
print(list1)

#length of list
print(len(list1))

#in
print("ram" in list1)

print("kohli" in list1)