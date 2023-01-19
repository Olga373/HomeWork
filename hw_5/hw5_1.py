def get_shortest(array: str) -> int:
    return len(min(array.split(), key=len))

print(get_shortest("hello word, I am python"))