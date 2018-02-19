class Sample(object):
    pass

x = Sample()
print(type(x))

class Dog(object):
    species = 'mammal'
    def __init__(self,breed,name,fur=True):
        self.breed = breed
        self.name = name
        self.fur = fur


sam = Dog(breed='Lab',name='Sammy')
sam1 = Dog(breed='Huskie',name='Sammy1')

print(type(sam))
print(type(sam1))
print(sam.breed)
print(sam1.breed)
print(sam.species)
print(sam.fur)






class Circle(object):
    pi = 3.14
    def __init__(self,radius=1,perimeter_val=1):
        self.radius = radius
        self.perimeter_val = 2*Circle.pi*perimeter_val;
    def area(self):
        return (self.radius**2) * Circle.pi
    def set_radius(self,new_radius):
        self.radius = new_radius
    def get_radius(self):
        return self.radius
    def perimeter(self):
        return 2*Circle.pi*self.radius


c= Circle(radius = 100)
print(c.pi)
#print(c.area())
print(c.perimeter())