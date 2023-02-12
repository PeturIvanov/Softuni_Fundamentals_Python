word = list(input())
index = 0
capital_letters = []
for ch in word:
    if 65 <= ord(ch) <= 90:
        capital_letters.append(index)

    index += 1

print(capital_letters)
