# [1, 2, 3, 3, 4, 5]
# [1, 2, 2, 3, 1] -> {1:2, 2:2, 3:1}
from random import randint

def random_list(start: int, end: int, count: int) -> None:
    random_list = []
    for _ in range(count):
        random_list.append(randint(start, end))
    print(random_list)
    return random_list



def count_same(n: int) -> int:

    counter = 0
    for num in set(n):
        if n.count(num) > 1:
            counter +=1
    return counter

print(count_same(random_list(start=1, end=10, count=7)))



