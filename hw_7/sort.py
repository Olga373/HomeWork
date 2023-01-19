# "is2 Thi1s T4est 3a"  ->  "Thi1s is2 3a T4est"

def get_digit(word: str) -> int or None:
    for symbol in word:
        if symbol.isdigit():
            return int(symbol)
    return None

def order(array: str) -> str:
    return ' '.join(sorted(array.split(), key=get_digit))

print(order("is2 Thi1s T4est 3a"))

#u1 = u'\u043f\u0440\u0438\u0432\u0435\u0442'
#print(u1)
