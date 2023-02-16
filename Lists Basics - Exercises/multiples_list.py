factor = int(input())
count = int(input())

result = []
number = factor
for _ in range(count):
    result.append(number)
    number += factor

print(result)
