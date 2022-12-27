
def factorial(num):
    numbers = list(range(1, num +1))
    result = 1
    for number in numbers:
        result *= number
    yield result

print(factorial(5))



