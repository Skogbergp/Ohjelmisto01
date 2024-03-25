class Dog:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

dog1 = Dog("Rufus")
dog2 = Dog("Milo")


print(dog1)
print(dog2)