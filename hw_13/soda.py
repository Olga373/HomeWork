
class Soda:
    def __init__(self, additive: str = None):
        self.additive = additive

    def __str__(self):
        return f"{self.additive}"

    def show_my_drink(self):
        if self.additive is None:
            return "Just soda"
        else:
            return f"Soda and {self.additive}"

soda_1 = Soda()
soda_2 = Soda("vanilla")


print(soda_1.show_my_drink())
print(soda_2.show_my_drink())