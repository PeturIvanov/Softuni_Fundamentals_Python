start = input()
end = input()
random_string = input()

found_character = []
random_string_as_numbers = [ord(char) for char in random_string]

for char_as_number in range(ord(start) + 1, ord(end)):
    if char_as_number in random_string_as_numbers:
        count = random_string_as_numbers.count(char_as_number)
        for number in range(count):
            found_character.append(char_as_number)

print(sum(found_character))