list_of_numbers = [int(x) for x in input().split()]
commands = input()
while commands != "end":
    data = commands.split()
    operator = data[0]
    if operator == "exchange":
        index = int(data[1])
        if 0 <= index < len(list_of_numbers):
            first_list = list_of_numbers[:index + 1]
            second_list = list_of_numbers[index + 1:]
            list_of_numbers = second_list + first_list
        else:
            print("Invalid index")
    elif operator == "max":
        even_or_odd = data[1]
        even_numbers = [n for n in list_of_numbers if n % 2 == 0]
        # max even
        if even_or_odd == "even":
            if even_numbers:
                max_even = max(even_numbers)
                count_max_even = list_of_numbers.count(max_even)
                if count_max_even == 1:
                    result = list_of_numbers.index(max_even)
                    print(result)
                elif count_max_even > 1:
                    result = 0
                    for idx in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[idx] == max_even:
                            result = idx
                            break
                    print(result)
            else:
                print("No matches")
        # max odd
        elif even_or_odd == "odd":
            odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
            if odd_numbers:
                max_odd = max(odd_numbers)
                count_max_odd = list_of_numbers.count(max_odd)
                if count_max_odd == 1:
                    result = list_of_numbers.index(max_odd)
                    print(result)
                elif count_max_odd > 1:
                    result = 0
                    for idx in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[idx] == max_odd:
                            result = idx
                            break
                    print(result)
            else:
                print("No matches")
    elif operator == "min":
        even_or_odd = data[1]
        even_numbers = [n for n in list_of_numbers if n % 2 == 0]
        # min even
        if even_or_odd == "even":
            if even_numbers:
                min_even = min(even_numbers)
                count_min_even = list_of_numbers.count(min_even)
                if count_min_even == 1:
                    result = list_of_numbers.index(min_even)
                    print(result)
                elif count_min_even > 1:
                    result = 0
                    for idx in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[idx] == min_even:
                            result = idx
                            break
                    print(result)
            else:
                print("No matches")
        # min odd
        elif even_or_odd == "odd":
            odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
            if odd_numbers:
                min_odd = min(odd_numbers)
                count_min_odd = list_of_numbers.count(min_odd)
                if count_min_odd == 1:
                    result = list_of_numbers.index(min_odd)
                    print(result)
                elif count_min_odd > 1:
                    result = 0
                    for idx in range(len(list_of_numbers) - 1, -1, -1):
                        if list_of_numbers[idx] == min_odd:
                            result = idx
                            break
                    print(result)
            else:
                print("No matches")
    elif operator == "first":
        count = int(data[1])
        even_or_odd = data[2]
        if even_or_odd == "even":
            even_numbers = [n for n in list_of_numbers if n % 2 == 0]
            if count > len(list_of_numbers):
                print("Invalid count")
            elif not even_numbers:
                print(even_numbers)
            elif count >= len(even_numbers):
                print(even_numbers)
            elif count < len(even_numbers):
                result = even_numbers[:count]
                print(result)
        elif even_or_odd == "odd":
            odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
            if count > len(list_of_numbers):
                print("Invalid count")
            elif not odd_numbers:
                print(odd_numbers)
            elif count >= len(odd_numbers):
                print(odd_numbers)
            elif count < len(odd_numbers):
                result = odd_numbers[:count]
                print(result)
    elif operator == "last":
        count = int(data[1])
        even_or_odd = data[2]
        if even_or_odd == "even":
            even_numbers = [n for n in list_of_numbers if n % 2 == 0]
            if count > len(list_of_numbers):
                print("Invalid count")
            elif not even_numbers:
                print(even_numbers)
            elif count >= len(even_numbers):
                print(even_numbers)
            elif count < len(even_numbers):
                reversed_nums = list(reversed(even_numbers))
                reverser_result = reversed_nums[:count]
                reverser_result.reverse()
                print(reverser_result)
        elif even_or_odd == "odd":
            odd_numbers = [n for n in list_of_numbers if n % 2 != 0]
            if count > len(list_of_numbers):
                print("Invalid count")
            elif not odd_numbers:
                print(odd_numbers)
            elif count >= len(odd_numbers):
                print(odd_numbers)
            elif count < len(odd_numbers):
                reversed_nums = list(reversed(odd_numbers))
                reverser_result = reversed_nums[:count]
                reverser_result.reverse()
                print(reverser_result)

    commands = input()
print(list_of_numbers)

