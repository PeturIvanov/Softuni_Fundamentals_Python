n = int(input())

is_balanced = False

counter = 0
for _ in range(n):
    string = input()

    if counter == 0 and string == ")":
        print("UNBALANCED")
        break

    if counter == 1 and string == "(":
        print("UNBALANCED")
        break

    if counter == 0 and string == "(":
        counter += 1

    if counter == 1 and string == ")":
        counter = 0
        is_balanced = True

if is_balanced:
    print("BALANCED")
