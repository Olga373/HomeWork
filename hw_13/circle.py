import math

class Circle:
    def __init__(self, radius):
        self.radius = float(radius)

    #def __str__(self):
        #return f"{self.side_a}, {self.side_b}, {self.side_c}"

    def square(self):
        return round(math.pi * (self.radius ** 2), 2)

    def perim(self):
        return round(2 * math.pi * self.radius, 2)

circle = Circle('4')
print(circle.perim())
#print(circle.square())