from string import ascii_lowercase
string = input().split()

total_sum = 0

for el in string:
    first_letter = el[0]
    last_letter = el[-1]
    digit = ""
    for char in el:
        if char.isdigit():
            digit += char

    first_letter_position = 0
    last_letter_position = 0

    for i, letter in enumerate(ascii_lowercase):
        if letter == first_letter.lower():
            first_letter_position = i + 1

        if letter == last_letter.lower():
            last_letter_position = i + 1

    result = 0
    if first_letter.isupper():
        result = int(digit) / first_letter_position

    else:
        result = int(digit) * first_letter_position

    if last_letter.isupper():
        result = result - last_letter_position

    else:
        result = last_letter_position + result

    total_sum += result

print(f"{total_sum:.2f}")
