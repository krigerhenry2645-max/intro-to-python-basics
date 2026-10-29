# oop
import math


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius * self.radius

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def print_details(self):
        print(f"Radius is {self.radius}")
        print(f"Area of circle is {self.get_area():.2f}")
        print(f"Perimeter of circle is {self.get_perimeter():.2f}")
        print("-" * 30)


circle1 = Circle(5)
circle2 = Circle(10)
circle3 = Circle(20)

print(circle1.get_area())
circle1.print_details()
circle2.print_details()
circle3.print_details()


#branches --copy-- master main
#we are going to learn inheritance in python