# Write a  Python program to create a person class.
# Include attributes like name, country and date of birth.
# Implement a method to determine the person's age.
from datetime import date
class PersonH:
    def __init__(self,name,dob,country):
        self.name = name
        self.dob = dob
        self.country = country

    def ddbb(self):
        today = date.today()
        age = today.year - self.dob.year
        y = today.year-age
        m = self.dob.month
        d = self.dob.day
        return y,m,d

    # def realDate(self):
    #     today = date.today()
    #     age = today.year - self.dob.year
    #     if today < date(today.year, self.dob.month, self.dob.day):
    #         age -= 1
    #     return age

    def age(self):
        return f"Hello {self.name} from {self.country};your dob is{self.ddbb()})"




h1 = PersonH('lilly',date(2002,4,9), "india")

print(h1.age())