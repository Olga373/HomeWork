class Cat:
    counter = True
    moor_counter = 0
    meow_counter = 0


    def __init__(self, name: str):
        self.name = name


    def to_answer(self):
        if Cat.counter:
            Cat.moor_counter += 1
            Cat.counter = False
            return f"{self.name}, Moor"
        else:
            Cat.meow_counter += 1
            Cat.counter = True
            return f"{self.name}, Meow"


    @staticmethod
    def count_moor():
        return Cat.moor_counter

    @staticmethod
    def count_meow():
        return Cat.meow_counter

cat_1 = Cat("Barsic")

print(cat_1.to_answer())
print(cat_1.to_answer())
print(cat_1.to_answer())
print(cat_1.to_answer())
print(cat_1.moor_counter)
print(cat_1.meow_counter)
