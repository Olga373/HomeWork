class Snow:
    def __init__(self, snowflake_count: int):
        self.snowflake_count = "*" * snowflake_count

    def __str__(self):
        return self.snowflake_count

    def __add__(self, other):
        return self.snowflake_count + "*" * other

    def __sub__(self, other):
        return "*" * (len(self.snowflake_count) - len('*' * other))

    def __mul__(self, other):
        return self.snowflake_count * other

    def __truediv__(self, other):
       return "*" * int((len(self.snowflake_count) / len('*' * other)))

    def makeSnow(self, snowflake_array: int):
        for _ in range(len(self.snowflake_count) // snowflake_array):
            print("*" * snowflake_array)
        print(len(self.snowflake_count) % snowflake_array * "*")



a = Snow(6)
print(a)
print(a.__add__(2))
print((a.__sub__(2)))
print(a.__mul__(2))
print(a.__truediv__(2))
print(a.makeSnow(5))





