series_of_string = input()

current_string = ""
multiply_number = ""
final_string = ""

for i, char in enumerate(series_of_string):
    if not char.isdigit():
        current_string += char

    elif char.isdigit():
        multiply_number += char
        if i + 1 < len(series_of_string):
            if series_of_string[i + 1].isdigit():
                continue

        final_string += current_string.upper() * int(multiply_number)
        multiply_number = ""
        current_string = ""


unique_symbols_used = ""
for char in final_string:
    if char not in unique_symbols_used:
        unique_symbols_used += char

print(f"Unique symbols used: {len(unique_symbols_used)}")
print(final_string)
