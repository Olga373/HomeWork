
def factorial(num):
    numbers = list(range(1, num +1))
    result = 1
    for number in numbers:
        result *= number
    yield result
f_1 = factorial(5)
print(f_1)


from functools import reduce
def factorial(namber):
    numbers = list(range(1, namber+1))
    factorial = reduce(lambda x, y: x * y, numbers)
    yield factorial

f_2 = factorial(5)
print(f_2)