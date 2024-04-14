# Write a  Python program to create a class representing a Circle.
# Include methods to calculate its area and perimete
import math

class Circle:
    def __init__(self,radius=None):
        self.radius = radius


    def area(self):
        r = self.radius
        return math.pi*(r*r)

    def perimeter(self):
        return 2*math.pi*self.radius



c1 = Circle(5.7)
print(c1.area())
print(c1.perimeter())



