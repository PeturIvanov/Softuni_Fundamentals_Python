numbers_list = []
for _ in range(3):
    number = int(input())
    numbers_list.append(number)


negative_counter = 0
zero_counter = 0
for num in numbers_list:
    if num == 0:
        zero_counter += 1
    if num < 0:
        negative_counter += 1


if zero_counter > 0:
    print("zero")

elif negative_counter == 1 or negative_counter == 3:
    print("negative")

else:
    print("positive")


