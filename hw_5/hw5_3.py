def is_isogram(array: str):
    if len(array.lower()) == len("".join(set(array.lower()))):
        return True
    else:
        return False

print(is_isogram(""))