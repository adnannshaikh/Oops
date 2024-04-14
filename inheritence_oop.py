class User:
    def sign_in(self):
        print('Logged in')

class Wizard(User):
    def __init__(self,name,power):
        self.name = name
        self.power = power

    def attack(self):
        print(f"Attacking with power of {self.power}")

class Archer(User):
    def __init__(self, name, arrow):
        self.name = name
        self.arrow = arrow

    def attack(self):
        print(f"Attacking with aarrows : arrows left -  {self.arrow}")

wizard1 = Wizard("zozo",50)
archer1 = Archer("bell",200)
# print(wizard1.sign_in())
wizard1.attack()
archer1.attack()

#Checking instances
print(isinstance(wizard1,Wizard))
print(isinstance(wizard1,object))#tells us that everything in python is an object and object is the base for every class created hereafter


#polymorphism
def player_attack(char):
    char.attack()

player_attack(wizard1)
player_attack(archer1)

print("------------------")
for char in [wizard1,archer1]:
    char.attack()