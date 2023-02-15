n = int(input())
word_to_find = input()

list_of_all = []
special_list = []
for _ in range(n):
    current_string = input()

    list_of_all.append(current_string)

    if word_to_find in current_string:
        special_list.append(current_string)

print(list_of_all)
print(special_list)
