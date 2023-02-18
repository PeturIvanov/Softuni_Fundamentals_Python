def solution(operator, first_num, second_num):
    result = 0
    if operator == "multiply":
        result = first_num * second_num
    elif operator == "divide":
        result = first_num // second_num
    elif operator == "add":
        result = first_num + second_num
    else:
        result = first_num - second_num

    return result


operators = input()
first_number = int(input())
second_number = int(input())

res = (solution(operators, first_number, second_number))
print(res)



