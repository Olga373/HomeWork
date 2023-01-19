#a = "1 9 3 4 -5"
def a_new(a: str) -> int:
    a_new = [int(i) for i in a.split()]
    return a_new

def min_max(a: list) -> int:

    num_min = min(a_new(a))
    num_max = max(a_new(a))
    #print(type(num_min))
    return [num_min, num_max]
print(min_max("1 9 3 4 -5"))




#print(min_max("1 9 3 4 -5"))
#print(num)