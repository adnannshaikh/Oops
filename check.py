'''
Creating an object car to specify some attributes and use some methods...
'''
class Car:
    def __init__(self,wheel=None,door=None,headlight=None):
        self.wheel = wheel
        self.door = door
        self.headlight = headlight

    def moveCar(self):
        dir = input("Enter the Direction: ")
        return f"Moving to {dir}"


car1 = Car()
car1.headlight = True
print(car1.headlight)
