string = input()
numbers_list = [int(n) for n in string if n.isdigit()]
string_list = [char for char in string if not char.isdigit()]

# take_list = [even for even in numbers_list if even % 2 == 0]
# skip_list = [odd for odd in numbers_list if odd % 2 != 0]

taken_string = ""
skipped_string = ""

for i, n in enumerate(numbers_list):
    if i % 2 == 0:
        taken_string += "".join(string_list[0:n])
        del string_list[:n]
    else:
        skipped_string += "".join(string_list[0:n])
        del string_list[:n]
print(taken_string)