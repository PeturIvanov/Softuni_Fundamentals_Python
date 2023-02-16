string_of_integers = input()
beggars = int(input())

list_of_numbers = string_of_integers.split(", ")
starting_list = [0] * beggars
# for _ in range(beggars):
#     starting_list.append(int(0))

index = 0
for el in list_of_numbers:
    starting_list[index] += int(el)
    index += 1
    if index == beggars:
        index = 0

print(starting_list)
