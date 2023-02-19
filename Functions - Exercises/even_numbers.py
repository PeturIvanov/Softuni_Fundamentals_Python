numbers = [int(n) for n in input().split()]
even_number = list(filter(lambda n: n % 2 == 0, numbers))
# even_number = [el for el in numbers if el % 2 == 0]
print(even_number)



# def is even(num):
#     result = num % 2 == 0
#     return result
#
#
# nums = [5, 4, 1, 8]
# print(list(filter(is_even, nums)))