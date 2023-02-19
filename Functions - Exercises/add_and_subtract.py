def sum_numbers(a, b):
    total_sum = a + b
    return total_sum


def subtract(total_sum, c):
    diff = (sum_numbers(a, b) - c)
    return diff


def add_and_subtract(a, b, c):
    result = subtract(sum_numbers(a, b), c)
    return result


a = int(input())
b = int(input())
c = int(input())

res = add_and_subtract(a, b, c)
print(res)

