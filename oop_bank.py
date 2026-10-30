# bank acc
from datetime import date, datetime


class Client:
    def __init__(self, names, kra_pin, DOB, gender):
        self.names = names
        self.kra_pin = kra_pin
        self.DOB = DOB  # Format: "2006-08-04" (YYYY-MM-DD)
        self.gender = gender

    def print_details(self):
        print(f"Names: {self.names}")
        print(f"KRA PIN: {self.kra_pin}")
        print(f"DOB: {self.DOB}")
        print(f"Gender: {self.gender}")
        print("-----------")

    def calc_age(self):
        today = date.today()
        # DOB is "YYYY-MM-DD", so parse it like that
        birth_date = datetime.strptime(self.DOB, "%Y-%m-%d").date()

        age = today.year - birth_date.year

        # If birthday hasn't happened yet this year, subtract 1
        if (today.month, today.day) < (birth_date.month, birth_date.day):
            age -= 1

        print(f"Age: {age} years")
        return age


class BankAccount:
    def __init__(self, owner, acc_no, balance):
        self.owner = owner
        self.acc_no = acc_no
        self.balance = balance

    def deposit(self, amount):
        self.balance += abs(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough money")
        else:
            self.balance -= abs(amount)

    def print_details(self):
        print(f"Owner: {self.owner.names}")
        print(f"Acc No: {self.acc_no}")
        print(f"Balance: {self.balance}")
        print("-----------")


# Create clients
Henry = Client("Henry Kriger", 'A0034', "2006-08-04", 'Male')
Ann = Client('Ann Mumbi', "A0035", '2000-01-15', 'Female')

# Create accounts
acc1 = BankAccount(Henry, "ACC001", 100)
acc2 = BankAccount(Ann, "ACC002", 200)
acc3 = BankAccount(Henry, "ACC003", 300)

acc1.deposit(10_000)
acc1.deposit(2000)
acc1.print_details()
acc1.withdraw(10_000)
acc1.print_details()

Henry.print_details()
Henry.calc_age()  # Now works
Ann.calc_age()

# Today's date - fixed
today = date.today()
print(f"Today: {today.day}/{today.month}/{today.year}")

accurate_age = today.year - today.month
print(f"Accurate age: {accurate_age}")