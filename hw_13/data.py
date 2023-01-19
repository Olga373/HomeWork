from dataclasses import dataclass
from typing import NamedTuple

class User:
    def __init__(self, name: str, surname: str, age: int):
        self.name = name
        self.surname = surname
        self.age = age

        def __str__(self):
            return f"{self.name}, {self.surname}, {self.age}

class UserAnnotation(NamedTuple):
    name: str
    surname: str
    age: int


@dataclass
class UserAnnotationDT:
    name: str
    surname: str
    age: int


