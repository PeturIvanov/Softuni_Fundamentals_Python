string = input()

result = " "

for char in string:
    if char != result[-1]:
        result += char

result = result.lstrip(" ")
print(result)