class Animal(object):
    def _init__(self):
        print("Animal Created")
    def whoAmI(self):
        print("Animal")
    def eat(self):
        print("Eating")


class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print("Dog created")

    def whoAmI(self):
        print("Dog")
    def bark(self):
        print("Woof!")
a = Animal()
print(a)
d = Dog()
print(d.whoAmI())
print(d.eat())
