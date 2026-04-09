from Encap1 import User
from Encap2 import User1
from Encap3 import User3

u1 = User()
u1.setName("Shrey")
result = u1.getName()
print(result)


u2 = User1("Max")
print(u2.getName())
u2.name = "Joy"
print(u2.getName())
u2.name = "Ekansh"
print(u2.name)

u3 = User3()
u3.setName("Shrey")
print(u3.getName())
#print(u3.__name)