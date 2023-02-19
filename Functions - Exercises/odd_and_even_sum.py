def odd_sum_even_sum(n):
    number_as_list = [int(num) for num in n]
    even_numbers = []
    odd_numbers = []
    for num in number_as_list:
        if num % 2 == 0:
            even_numbers.append(num)
        elif num % 2 != 0:
            odd_numbers.append(num)

    even_sum = sum(even_numbers)
    odd_sum = sum(odd_numbers)
    print(f"Odd sum = {odd_sum}, Even sum = {even_sum}")


number = input()
odd_sum_even_sum(number)
