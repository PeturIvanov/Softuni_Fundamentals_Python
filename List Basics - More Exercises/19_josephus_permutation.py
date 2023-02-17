people = [int(x) for x in input().split()]
k = int(input())
result = []

steps = 0
index = 0
while people:
    steps += 1

    if steps % k == 0:
        result.append(people[index])
        people.pop(index)
    elif steps % k != 0:
        index += 1

    if index >= len(people):
        index = 0
print(str(result).replace(" ", ""))
