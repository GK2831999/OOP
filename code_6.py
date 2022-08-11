import math


class Shape3D:
    pi = 3.14159
    def __init__(self, name = 'Default', radius = 0):
        self._area = 0
        self._name = name
        self._height = 'No need'
        self._radius = radius

class Sphere:
    def __init__(self,name,rad):
        self.name = name   
        self.rad = rad
        print(f"Shape name: {self.name}, Area Formula: 4 * pi * r* r")
    def calc_surface_area(self):
        print(f"Area: {4*math.pi*self.rad*self.rad}")
    def __str__(self):
        return f"Radius {self.rad}, Height : No Need"
class Cylinder:
    def __init__(self,name,rad,height):
        self.name = name   
        self.rad = rad
        self.height =  height 
        print(f"Shape name: {self.name}, 2 * pi *r * (r + h)")
    def calc_surface_area(self):
        print(f"Area: {2*math.pi*self.rad*(self.rad+self.height)}")
    def __str__(self):
        return f"Radius {self.rad}, Height :{self.height}"


def calc_surface_area(self):
    return 2 * Shape3D.pi * self._radius
def __str__(self):
    return "Radius: "+str(self._radius)
sph = Sphere('Sphere', 5)
print('----------------------------------')
sph.calc_surface_area()
print(sph)
print('==================================')
cyl = Cylinder('Cylinder', 5, 10)
print('----------------------------------')
cyl.calc_surface_area()
print(cyl)