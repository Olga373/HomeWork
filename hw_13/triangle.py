from annotation import TringleAnnotation
import math

class Triangle:
    def __init__(self, side_a: int, side_b: int, side_c: int):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    #def __str__(self):
        #return f"{self.side_a}, {self.side_b}, {self.side_c}"


    def square(self):
        a = int(self.side_a)
        b = int(self.side_b)
        c = int(self.side_c)
        p = a + b + c
        square = round(math.sqrt(p * (p - a) * (p - b) * (p - c)), 2)
        return square

    def perim(self):
        a = self.side_a
        b = self.side_b
        c = self.side_c
        perim = a + b + c
        return perim

triangle = Triangle("2", "1", "4")

print(triangle.square())
#print(triangle.perim())