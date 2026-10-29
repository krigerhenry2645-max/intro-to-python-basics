from arrays import people


def add(a,b,c):
    res = a+b+c
    return res

def addition(*nums):
    """Returns sum of nums
    Parameters:intergers or floats or a mix of integers and floats
    Returns:Integer or float or a mix of integers and floats"""
    total = sum(nums)
    return total

def build_profile(**kwargs): # dict key-word args
    for k,w in kwargs.items():
        print(f"{k} : {w}")

def fancy_function(name, *nums, **kwargs):
    print(f"{name} : {nums}")
    print(f"Extra info: {kwargs}")

# build_profile(experience="100", name="Jane", proffession="Programming", gender="Male")

# normal function
def square(num):
    return num*num

result = square(5)
print(result)

# lambda (anonymous) - same thing shorter
square_lambda = lambda num: num*num
print(square_lambda(5))
print(square_lambda(3.5))

# cylinder surface area = 2πr² + 2πrh
surface_area_cylinder = lambda r,h: 2 * (22/7) * r**2 + 2 * (22/7) * r * h
# OR simpler: lambda r,h: 2 * (22/7) * r * (r + h)

# CORRECT CALL - use = not :
print(surface_area_cylinder(r=7, h=20))
# Output: 1188.0

people=[
    {
        "name" : "Alex","age":30 },
    {
        "name" : "Bob","age":25 },
    {
        "name" : "Charlie","age":35 }

]
sorted_people = sorted(people, key=lambda p: p["age"])
print(sorted_people)