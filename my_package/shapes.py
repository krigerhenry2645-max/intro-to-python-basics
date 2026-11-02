def triangle_area(a,b,c):
    s = (a+b+c)/2
    area = s*(s-a)*(s-b)*(s-c)
    return area**0.5