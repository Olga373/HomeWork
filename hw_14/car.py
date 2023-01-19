class Car:
    instance_counter = 0

    def __init__(self, milaege: int, name: str, year: int, price: int):
        self.milaege = milaege
        self.name = name
        self.year = year
        self.price = price
        Car.instance_counter += 1

    def __eq__(self, other):
        if self.name == other.name and self.year == other.year:
            return True
        else:
            return False

    def __str__(self):
        return f"Name: {self.name}, year:{self.year}, Price: {self.price}"

    def get_price(self):
        return f"Price: {self.price}USD - {self.price * 2.5}BYN"

    @classmethod
    def get_instance_count(cls):
        return cls.instance_counter

    @staticmethod
    def get_country(brand):
        if brand in["BMW", "AUDI"]:
            return "Germany"
        else:
            return "Unknown country"

    @property
    def miles(self):
        return self.milaege

    @miles.setter
    def miles(self, new_mileage_value):
        self.milaege = new_mileage_value

    @miles.deleter
    def miles(self):
        print("Mileage ib null")
        self.milaege = None



car_1 = Car(milaege=100_000, name="AUDI", year=2008, price=15000)
car_2 = Car(milaege=150_000, name="AUDI", year=2008, price=25000)

print(Car.get_instance_count())
print(Car.get_country("AUDI"))
print(car_2.get_price())


class Chevrolet(Car):
    instance_counter = 0

    def get_country(self):
        return "USA"

car_chevrolet = Chevrolet(10000, "Taho", year=2005, price=20000)

print(car_chevrolet.get_country())
print(car_chevrolet.get_instance_count())