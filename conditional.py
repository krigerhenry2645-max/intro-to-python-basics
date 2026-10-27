# if else
import sys

name = input("Enter you Name:")
age = input("Enter your age: ")
if not age.isnumeric():
    print("Invalid Age")
    #TERMINATE
    sys.exit()

if int(age )>= 18:
    print(name+"is old enough to be an adult")
else:
    print(name + " You are child")