class Car:

    name = "Shrey"                        #it will be the same for all the instances if we not created any constructor

    def __init__(self, name):               #self = current object
        self.name = name


c1 = Car("Max")
print(c1.name)