string = input()
digits = ""
letters = ""
other_char = ""

for char in string:
    if char.isalpha():
        letters += char
    elif char.isdigit():
        digits += char
    else:
        other_char += char

print(digits)
print(letters)
print(other_char)