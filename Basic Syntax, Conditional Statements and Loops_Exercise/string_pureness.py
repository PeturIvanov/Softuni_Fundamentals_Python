n = int(input())

for _ in range(n):
    string = input()

    pure = True

    for i in string:
        if i == ',' or i == '.' or i == '_':
            pure = False

    if pure:
        print(f'{string} is pure.')
    else:
        print(f'{string} is not pure!')
