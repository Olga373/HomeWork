numbers = input("Enter numbers: ")
list_numbers = numbers.split(",")
tuple_numbers = tuple(list_numbers)

print(list_numbers, type(list_numbers))
print(tuple_numbers, type(tuple_numbers))
