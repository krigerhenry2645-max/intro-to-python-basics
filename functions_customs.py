from unittest import result


def great():
    print("hello!")

def     greating(name):
    print(f"Hello {name}")

def volume_cylinder(radius,height):
    v =22/7 * radius**2*height
    print(round(v,2))

def volume_cylinder_better (radius,height):
    v =22/7 * radius**2*height
    return round(v,2)
    #
    # greating('Tegan')
    # greating('Hum')
result= volume_cylinder_better(6.7,8)
print(result)

with open("volumes.text","w") as file:
    file.write(str(result))

#volume_cylinder(10,9)
#volume_cylinder(8,9)

def divide(a=1,b=2,should_round=False):
    result = a/b
    if should_round == True:
        return round(result,2)
    else:
        return result

print(divide(2,3,True))
print(divide(b=7))