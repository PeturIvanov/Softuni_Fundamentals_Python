def tribonacci_sequence(num):
    result = [1, ]
    list_of_numbers = [0, 0, 1]
    number = 1
    for _ in range(1, num):
        number_to_add = sum(list_of_numbers)
        result.append(number_to_add)
        list_of_numbers.remove(list_of_numbers[0])
        list_of_numbers.append(number_to_add)

    return result


counter = int(input())
res = tribonacci_sequence(counter)
result_as_str = [str(x) for x in res]
print(" ".join(result_as_str))
