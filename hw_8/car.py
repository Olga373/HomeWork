class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def __str__(self):
        return f"{self.color}{self.type}{self.year}"

    def started (self):
        return f"The car started"

    def car_off (self):
        return f"The car turned off"



car_1 = Car(color="red ", type="sport_car ", year="2020")
car_2 = Car(color="black ", type="sedan ", year="2015")

print(car_1)
print(car_1.started())
print(car_2)
print(car_2.car_off())