import string
from functools import reduce
print(string.ascii_lowercase)

def get_numbers(array: str) -> str:
    numbers = [string.ascii_lowercase.index(char.lower()) + 1 for char in array
               if char.lower() in string.ascii_lowercase]
    output = reduce(lambda x, y: f"{x}{y}", numbers)
    return output
print(get_numbers("fhgfh jhgjhgk"))
