def positive_integer(num: int) -> int:
    k = 0
    for i in range(2, num - 1):
        if num % i == 0:
            k += 1
    if k == 0:
        return True
    else:
        return False

print(positive_integer(2))

