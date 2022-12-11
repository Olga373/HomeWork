class Rectagle:
    def __init__(self, side_a, side_b):
        self.side_a = int(side_a)
        self.side_b = int(side_b)

    #def __str__(self):
        #return f"{self.side_a}, {self.side_b}, {self.side_c}"

    def square(self):
        return self.side_a * self.side_b

    def perim(self):
        return (self.side_a + self.side_b) * 2

rectangle = Rectagle("4", "2")
#print(rectangle.perim())
#print(rectangle.square())

