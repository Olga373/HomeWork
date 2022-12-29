class Snow:
    def __init__(self, snowflake_count: int):
        self.snowflake_count = snowflake_count

    #def __str__(self):
        #return self.snowflake_count

    def __add__(self, other):
        self.snowflake_count += other

    def __sub__(self, other):
        self.snowflake_count -= other

    def __mul__(self, other):
        self.snowflake_count *= other

    def __truediv__(self, other):
       self.snowflake_count /= other

    def makeSnow(self, snowflake_array: int):
        for _ in range(self.snowflake_count // snowflake_array):
            print("*" * snowflake_array)
        print(self.snowflake_count % snowflake_array * "*")



snow = Snow(100)
snow -5

print(snow.snowflake_count)
print(snow.makeSnow(5))





