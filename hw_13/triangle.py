
import math

def triangle_square(a, b, c):
    p = sum([a, b, c])
    square = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
    return square

def triangle_perim(a, b, c):
    perim = sum([a, b, c])
    return perim


#print(triangle_square(1, 2, 3), triangle_perim(1, 2, 3))
