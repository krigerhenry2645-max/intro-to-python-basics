# inheritance

class Employee:
    def __init__(self, name, email, age, department, salary):  # constructor
        self.name = name
        self.email = email
        self.age = age
        self.department = department
        self.salary = salary

    def show_details(self):
        print(
            f"Name: {self.name}, Email: {self.email}, Age: {self.age}, Dept: {self.department}, Salary: {self.salary}")


class PermanentEmployee(Employee):  # inheriting
    def __init__(self, name, email, age, department, salary, cover, increment):
        super().__init__(name, email, age, department, salary)  # you were missing age here
        self.cover = cover
        self.increment = increment

    def show_details(self):
        super().show_details()
        print(f"Cover: {self.cover}, Increment: {self.increment}")
        print("-----------")


class ContractEmployee(Employee):
    def __init__(self, name, email, age, department, salary, tenure):
        super().__init__(name, email, age, department, salary)  # fixed indent
        self.tenure = tenure  # was self tenure (missing dot)

    def show_details(self):
        super().show_details()
        print(f"Tenure: {self.tenure} months")
        print("-----------")


# Test it
p1 = PermanentEmployee("Henry", "henry@company.com", 20, "IT", 50000, "Medical", 5000)
c1 = ContractEmployee("Ann", "ann@company.com", 26, "HR", 30000, 12)

p1.show_details()
c1.show_details()

#TODO OVERRIDING
#oop in python