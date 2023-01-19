def sum_range(a:int, b: int) -> int:
    if a > b:
        a, b = b, a
    lst = list(range(a, b + 1))
    print(lst)
    return sum(lst)
sum_range(10, 5)

