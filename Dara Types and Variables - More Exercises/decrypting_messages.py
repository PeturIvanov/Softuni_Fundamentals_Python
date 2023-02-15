key = int(input())
n = int(input())

for _ in range(n):
    letter = ord(input())
    key_letter = letter + key
    print(f"{chr(key_letter)}", end="")
