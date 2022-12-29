import sys

def fib(n: int):
    fib_1 = fib_2 = 1
    print(fib_1, fib_2, end=' ')
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        print(fib_2, end=' ')

f_1 = fib(10)
print(f_1)
print(sys.getsizeof(f_1))

def gen_fib(n: int):
    fib_1 = fib_2 = 1
    yield (fib_1, fib_2)
    for i in range(2, n):
        fib_1, fib_2 = fib_2, fib_1 + fib_2
        yield (fib_2)


f_2 = gen_fib(10)
print(f_2)
print(sys.getsizeof(f_2))
