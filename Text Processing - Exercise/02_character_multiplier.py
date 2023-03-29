def multiply(long_string, short_string):
    result = 0
    for i in range(len(short_string)):
        result += ord(short_string[i]) * ord(long_string[i])
    for i in range(len(short_string), len(long_string)):
        result += ord(long_string[i])
    return result


string_one, string_two = input().split()
total_sum = 0
if len(string_one) == len(string_two):
    total_sum += multiply(string_one, string_two)

else:
    if len(string_one) > len(string_two):
        total_sum += multiply(string_one, string_two)
    elif len(string_two) > len(string_one):
        total_sum += multiply(string_two, string_one)
print(total_sum)
