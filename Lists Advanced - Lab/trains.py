wagons_count = int(input())

train = [0] * wagons_count

command = input()

while command != "End":
    input_data = command.split()
    people = int(input_data[-1])

    if command.startswith("add"):
        train[-1] += people
    elif command.startswith("insert"):
        index = int(input_data[1])
        train[index] += people
    elif command.startswith("leave"):
        index = int(input_data[1])
        train[index] -= people

    command = input()

print(train)
