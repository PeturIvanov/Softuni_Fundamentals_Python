first_input_line = input().split(", ")
second_input_line = input().split(", ")

result = []

for el in first_input_line:
    for elem in second_input_line:
        if el in elem:
            result.append(el)
            break

print(result)
