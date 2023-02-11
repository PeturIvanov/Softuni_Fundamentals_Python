first_string = input()
second_string = input()

word = first_string

for idx in range(len(first_string)):
    if first_string[idx] == second_string[idx]:
        continue

    word = second_string[:idx + 1] + first_string[idx + 1:]
    print(f"{word}")
