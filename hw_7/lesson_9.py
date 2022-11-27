'''class Human:
    _class_name = "Human"

    def __init__(self, name, surname, age, profatoin):
        self.name = name
        self.surname = surname
        self.age = age
        self.profatoin = profatoin


person_1 = Human(name='Walter', surname='White', age=50, profatoin='Teacher')
print(Human._class_name)'''

'''lass Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return f"x={self.x + other.x}, y = {self.y + other.y}"

point_1 = Point(x=3, y=5)
point_2 = Point(x=1, y=6)

print(point_1 + point_2)'''

class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"{}"

