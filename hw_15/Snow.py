class Snow:
    def __init__(self, n: int):
        self.n = "*" * n

    def __str__(self):
        return self.n

    def __add__(self, n):
        return self.n + "*" * n

    def __sub__(self, n):
        return "*" * (len(self.n) - len('*' * n))

    def __mul__(self, n):
        return self.n * n

    def __truediv__(self, n):
       return "*" * int((len(self.n) / len('*' * n)))

    def makeSnow(self, k):
        s = (self.n + '\\n') * k
        return s

a = Snow(6)
print(a)
print(a.__add__(2))
print((a.__sub__(2)))
print(a.__mul__(2))
print(a.__truediv__(2))
print(a.makeSnow(5))





