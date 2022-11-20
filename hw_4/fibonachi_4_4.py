def fib(n: int):
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end= ' ')
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')

fib(10)

