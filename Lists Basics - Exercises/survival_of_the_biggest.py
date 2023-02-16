list_of_integers = [int(x) for x in input().split()]
n = int(input())

for _ in range(n):
    list_of_integers.remove(min(list_of_integers))

result = []

for el in list_of_integers:
    result.append(str(el))

print(", ".join(result))
