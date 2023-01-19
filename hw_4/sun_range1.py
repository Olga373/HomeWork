from random import sample

def sum_range(start: int, end: int, count: int) -> list:
    g = range(start, end + 1)
    random_g = sample(g, count)
    return random_g

print(sum_range(1, 4, 4))

def sum_range_2(lst: list, value: int) -> list:
    values = []
    for num in lst:
        if num % 2 == 0:
            values.append(num)
    return sum(values)

print(sum_range_2(lst=sum_range(start=1, end=100, count=25), value=30))

