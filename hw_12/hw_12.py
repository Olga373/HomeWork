from annot import UserAnnotation
import datetime
now = datetime.datetime.now()
now = int(now.year)
#print(now)

class User:
    def __init__(self, name: str, surname: str, age: int, country: str, gender: str, professoin: str):
        self.name = name
        self.surname = surname
        self.age = age
        self.county = country
        self.gender = gender
        self.profession = professoin

    def __str__(self):
        return f"{self.name}, {self.surname}, {self.age}, {self.gender}, {self.county}, {self.profession}"



    def birth_year(self) -> UserAnnotation:
        return f"{now - self.age}"


    def email(self) -> UserAnnotation:
        return f"{self.name + self.surname}@gmail.ru"


    def doctor(self):
        doctor = User.__str__(self)
        return doctor

    def policeman(self):
        policeman = User.__str__(self)
        return policeman

    def teacher(self):
        teacher = User.__str__(self)
        return teacher

user_1 = User(name="Nik", surname="Black", age=39, country="UK", gender="m", professoin="doctor")
user_2 = User("Tom", "Short", 40, "USA", "m", "policeman")
user_3 = User("Kate", "Corn", 26, "France", "w", "teacher")


#print(user_1)
print(user_1.birth_year())
print(user_1.email())
print(user_1.doctor())

print(user_2.birth_year())
print(user_2.email())
print(user_2.policeman())

print(user_3.birth_year())
print(user_3.email())
print(user_3.teacher())

