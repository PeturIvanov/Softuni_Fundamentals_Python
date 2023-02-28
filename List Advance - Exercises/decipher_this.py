secret_message = input().split()

for word in secret_message:
    first_letter = ""
    remaining_letters = []
    for char in word:
        # if 47 < ord(char) < 58:
        if char.isdigit():
            first_letter += char
        else:
            remaining_letters.append(char)

    remaining_letters[0], remaining_letters[-1] = remaining_letters[-1], remaining_letters[0]
    secret_word = "".join(remaining_letters)
    result = chr(int(first_letter)) + secret_word
    print(result, end=" ")

