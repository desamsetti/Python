class Line(object):
    def __init__(self,coor1=(0,0),coor2=(0,0)):
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        x1,y1 = self.coor1
        x2,y2 = self.coor2
        x = x2-x1
        y = y2-y1
        x = x**2
        y = y**2
        final = (x+y)**0.5
        return final

    def slope(self):
        s2 = self.coor2[1]-self.coor2[0]
        s1 = self.coor1[1]-self.coor1[0]
        s=s2/s1
        return s

li = Line((3,2),(8,10))
print(li.distance())
print(li.slope())






class Cylinder(object):
    def __init__(self,height=1,radius=1):
        self.height = height
        self.radius = radius
    def volume(self):
        return 3.14*self.radius*self.radius*self.height

    def surface_area(self):
        return (2*3.14*self.radius*self.height)+(2*3.14*self.radius*self.radius)


c = Cylinder(2,3)
print(c.volume())
print(c.surface_area())