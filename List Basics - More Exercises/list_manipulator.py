def max_even_odd_function(list_even_odd):
    if list_even_odd:
        max_even_odd = max(list_even_odd)
        count_even_odd = list_of_numbers.count(max_even_odd)
        if count_even_odd == 1:
            print(list_of_numbers.index(max_even_odd))
        elif count_even_odd > 1:
            for idx in range(len(list_of_numbers) - 1, -1, -1):
                if list_of_numbers[idx] == max_even_odd:
                    print(idx)
                    break
    else:
        print("No matches")


def min_even_odd_function(list_odd_even):
    if list_odd_even:
        min_odd_even = min(list_odd_even)
        count_odd_even = list_of_numbers.count(min_odd_even)
        if count_odd_even == 1:
            print(list_of_numbers.index(min_odd_even))
        elif count_odd_even > 1:
            for idx in range(len(list_of_numbers) - 1, -1, -1):
                if list_of_numbers[idx] == min_odd_even:
                    print(idx)
                    break
    else:
        print("No matches")


def first_even_odd(odd_even_numbers, count):
    if count > len(list_of_numbers):
        print("Invalid count")
    elif not odd_even_numbers:
        print(even_numbers)
    elif count >= len(odd_even_numbers):
        print(odd_even_numbers)
    elif count < len(odd_even_numbers):
        print(odd_even_numbers[:count])


def last_even_odd(even_odd_numbers, count):
    if count > len(list_of_numbers):
        print("Invalid count")
    elif not even_odd_numbers:
        print(even_odd_numbers)
    elif count >= len(even_odd_numbers):
        print(even_odd_numbers)
    elif count < len(even_odd_numbers):
        reversed_nums = list(reversed(even_odd_numbers))
        reverser_result = reversed_nums[:count]
        reverser_result.reverse()
        print(reverser_result)


list_of_numbers = [int(x) for x in input().split()]
commands = input()
even_numbers = [n for n in list_of_numbers if n % 2 == 0]
odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
while commands != "end":
    data = commands.split()
    operator = data[0]
    # exchange
    if operator == "exchange":
        index = int(data[1])
        if 0 <= index < len(list_of_numbers):
            first_list = list_of_numbers[:index + 1]
            second_list = list_of_numbers[index + 1:]
            list_of_numbers = second_list + first_list
            even_numbers = [n for n in list_of_numbers if n % 2 == 0]
            odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
        else:
            print("Invalid index")
    elif operator == "max":
        even_or_odd = data[1]
        # max even
        if even_or_odd == "even":
            max_even_odd_function(even_numbers)
        # max odd
        elif even_or_odd == "odd":
            max_even_odd_function(odd_numbers)
    elif operator == "min":
        even_or_odd = data[1]
        # min even
        if even_or_odd == "even":
            min_even_odd_function(even_numbers)
        # min odd
        elif even_or_odd == "odd":
            min_even_odd_function(odd_numbers)
    elif operator == "first":
        count = int(data[1])
        even_or_odd = data[2]
        # first even
        if even_or_odd == "even":
            first_even_odd(even_numbers, count)
        # first odd
        elif even_or_odd == "odd":
            first_even_odd(odd_numbers, count)
    elif operator == "last":
        count = int(data[1])
        even_or_odd = data[2]
        # last even
        if even_or_odd == "even":
            last_even_odd(even_numbers, count)
        # last odd
        elif even_or_odd == "odd":
            last_even_odd(odd_numbers, count)
    commands = input()
print(list_of_numbers)

