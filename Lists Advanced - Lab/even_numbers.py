# numbers = [int(n) for n in input().split(", ")]
#
# even_numbers_index = []
#
# for i in range(len(numbers)):
#     if numbers[i] % 2 == 0:
#         even_numbers_index.append(i)
#
# print(even_numbers_index)


# numbers = [int(n) for n in input().split(", ")]
# even_or_odd = [el if el % 2 == 0 else "no" for el in numbers]
# result = list(filter(lambda x: x != "no", even_or_odd))
# print(result)


# numbers = [int(num) for num in input().split(", ")]
# # even_numbers_index = [numbers.index(el) for el in numbers if el % 2 == 0]
# even_numbers_index = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
# print(even_numbers_index)


numbers = [int(num) for num in input().split(", ")]
even_numbers_index = [i for i, k in enumerate(numbers) if k % 2 == 0]
print(even_numbers_index)