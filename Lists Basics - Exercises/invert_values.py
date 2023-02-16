string_of_numbers = input()

list_of_numbers = string_of_numbers.split()
result = []

for el in list_of_numbers:

    if int(el) > 0:
        opposite_number = -int(el)
        result.append(opposite_number)
    elif int(el) < 0:
        opposite_number = abs(int(el))
        result.append(opposite_number)
    else:
        result.append(int(el))

print(result)
