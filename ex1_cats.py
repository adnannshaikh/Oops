#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
cat1 = Cat("harry",12)
cat2 = Cat("tom",11)
cat3 = Cat("larry",10)



# 2 Create a function that finds the oldest cat

def old_cat(*args):
    return max(args)

# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f"The Oldest Cat is {old_cat(cat1.age,cat2.age,cat3.age)} years old")