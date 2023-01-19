#11 -> 22
#188 -> 191
#191 -> 202
#2541 -> 2552

def get_next_palidrom(value: int):
    value += 1
    while str(value) != str(value)[::-1]:
        value += 1
    return value
print(get_next_palidrom(11))