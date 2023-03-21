words = input().split()
result_string = ""

for el in words:
    result_string += el * len(el)

print(result_string)