chars_list = [char for char in input() if char != " "]
default = 0

chars = dict.fromkeys(chars_list, default)

for char in chars_list:
    chars[char] += 1

for char, occurrences in chars.items():
    print(f"{char} -> {occurrences}")
