from math import ceil

list_of_numbers = [int(n) for n in input().split(", ")]

counter = 0

for decade in range(10, ceil(max(list_of_numbers)) + 10, 10):
    result = []
    for num in list_of_numbers:
        if decade >= num > counter:
            result.append(num)

    for remove in result:
        list_of_numbers.remove(remove)
    print(f"Group of {decade}'s: {result}")
    counter += 10

