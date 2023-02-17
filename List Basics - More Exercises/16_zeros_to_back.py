numbers = [int(x) for x in input().split(", ")]
result = []


for el in numbers:
    if el == 0:
        numbers.remove(el)
        numbers.append(el)

print(numbers)
