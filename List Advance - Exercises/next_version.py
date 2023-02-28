x, y, z = [int(num) for num in input().split(".")]

z += 1
if z == 10:
    z = 0
    y += 1

    if y == 10:
        y = 0
        x += 1

print(f"{x}.{y}.{z}")
