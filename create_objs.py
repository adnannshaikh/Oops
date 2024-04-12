# OOP
# wizard game kinda like harrypotter

class PlayerCharacter:

    membership = True #class object attribute

    def __init__(self,name,age):#self refers to the main object itself(ie PLayerCharacter)
        '''
        #__init__ is a special method(dunder method)
        __init__ is also a constructor method
        '''

        self.name = name #these are attributes
        self.age = age


    def run(self):
        print("Run")
        return "Done"



player1 = PlayerCharacter('adnan',22)
player2 = PlayerCharacter('cody',22)
player2.attack = 200

print(player1.name,player1.age,player1.run())
print(f"{player2.name}'s attack power is {player2.attack}")