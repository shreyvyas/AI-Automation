print("Joy")

str = "Max and Joy"
print(str)

print(str.count("o"))

print(str.isdigit())

print(str.upper())

print(str.lower())

print(str.capitalize())            #it makes first letter uppercase and rest lowercase

print(len(str))

print(str.index("M"))

str1 = " max and joy "

#print(str1.strip())

if(str1.strip()=="Max and Joy"):
    print("pass")

else:
    print("fail")


str3 = "max"
str4 = "joy"

print(str3.join(str4))     #join is normally used with list, not with single string

print(str3 + " "  + str4)

print(str4.startswith("j"))

print(str3.endswith("x"))

print(str3.endswith("y"))

myStr = "abcdefghijk"
print(myStr[0])

myStr[0] = 'x'
print(myStr)