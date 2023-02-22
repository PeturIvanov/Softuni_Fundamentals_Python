def solve(a, b):
    result = None
    if a == "int":
        b = int(b)
        result = b * 2
    elif a == "real":
        b = int(b)
        multiply = b * 1.5
        result = f"{multiply:.2f}"
    else:
        result = f"${b}$"

    return result


command = input()
input_string = input()

res = solve(command, input_string)
print(res)
