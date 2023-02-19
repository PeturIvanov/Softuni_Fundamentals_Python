def find_smallest(a, b, c):
    numbers_as_string = [a, b, c]
    numbers = [int(num) for num in numbers_as_string]
    result = min(numbers)
    return result


number_one = input()
number_two = input()
number_three = input()

min_number = find_smallest(number_one, number_two, number_three)
print(min_number)
