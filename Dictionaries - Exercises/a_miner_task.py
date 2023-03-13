command = input()

resources = {}

while command != "stop":
    quantity = int(input())

    if command not in resources:
        resources[command] = quantity
    else:
        resources[command] += quantity

    command = input()
for resource, quantity in resources.items():
    print(f"{resource} -> {quantity}")
