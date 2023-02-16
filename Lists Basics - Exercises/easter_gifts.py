list_of_gifts = input().split()

command = input()

# fruits = ['apple', 'banana', 'cherry']
#
# x = fruits.index("cherry")

while command != "No Money":
    command_list = command.split()

    if command_list[0] == "OutOfStock":
        for el in list_of_gifts:
            if el == command_list[1]:
                idx = list_of_gifts.index(el)
                list_of_gifts[idx] = "None"

    elif command_list[0] == "Required":
        if int(command_list[2]) <= len(list_of_gifts):
            for idx in range(len(list_of_gifts)):
                if int(command_list[2]) == idx:
                    list_of_gifts[idx] = command_list[1]

    elif command_list[0] == "JustInCase":
        list_of_gifts[-1] = command_list[1]

    command = input()

result = []

for el in list_of_gifts:
    if el != "None":
        result.append(el)

print(" ".join(result))
