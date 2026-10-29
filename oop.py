# Object Oriented Programming
# is all about organizing our code nicely
# it entails security

class Person:
    # constructor
    def __init__(self, name, DOB, weight, height, age):
        self.name = name
        self.age = age
        self.DOB = DOB
        self.weight = weight
        self.height = height

    def display(self):
        print(f"Name is {self.name} and DOB is {self.DOB}")
        print(f"Age: {self.age}, Weight: {self.weight}, Height: {self.height}")

    def get_bmi(self):  # <- must be same level as display(), not inside it
        # height is in cm, so convert to meters
        height_m = self.height / 100
        bmi = self.weight / (height_m ** 2)
        return round(bmi, 2)

# How to use it:
person1 = Person(name="John", DOB="2000-01-01", weight=70, height=175, age=25)
person1.display()
print(f"{person1.name}'s BMI is {person1.get_bmi()}\n")

person2 = Person(name="Henry", DOB="2006-08-01", weight=60, height=165, age=20)
person2.display()
print(f"{person2.name}'s BMI is {person2.get_bmi()}")