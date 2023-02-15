n = int(input())

list_of_numbers = []

for _ in range(n):
    number = int(input())

    list_of_numbers.append(number)

command = input()
result = []

for el in list_of_numbers:

    if command == "even":
        if el % 2 == 0:
            result.append(el)
    if command == "odd":
        if el % 2 == 1:
            result.append(el)
    if command == "negative":
        if el < 0:
            result.append(el)
    if command == "positive":
        if el >= 0:
            result.append(el)

print(result)
