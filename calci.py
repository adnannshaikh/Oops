#Write a  Python program to create a calculator class.
#Include methods for basic arithmetic operations.

class Calculator:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def addition(self):
        return self.x + self.y

    def subtraction(self):
        return self.x - self.y

    def multiplication(self):
        return self.x * self.y

    def division(self):
        if self.y!=0:
            return self.x / self.y
        else:
            return "Can't divide with zero"



c = Calculator(2,4)
 #Better way is to remove __init__ and directly create a method
# result1 = c.addition(2,3)
print(c.division())