import math

def circle_square(radius):
    return round(math.pi * (radius ** 2), 2)

def circle_perim(radius):
    return round(2 * math.pi * radius, 2)

#print(circle_perim(5), circle_square(5))