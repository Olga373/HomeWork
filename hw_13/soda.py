
class Soda:
    def __init__(self, additive: str):
        self.additive = additive


    def __str__(self):
        return f"{self.additive}"

    def show_my_drink(self):
        if self.additive == "wihtout_additive":
            print(f"Regular soda")
        else:
            print(f"Soda and {Soda.__str__(self)}")


soda_1 = Soda("without_additive")
soda_2 = Soda("vanilla")


print(soda_1.show_my_drink())
print(soda_2.show_my_drink())