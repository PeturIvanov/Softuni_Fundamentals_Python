sequence_of_numbers = [int(x) for x in input().split()]

left_car_time = 0
right_car_time = 0

index = 0

for idx in range(len(sequence_of_numbers) // 2):
    if sequence_of_numbers[idx] == 0:
        left_car_time = left_car_time * 0.8

    left_car_time += sequence_of_numbers[idx]

for idx in range(-1, -len(sequence_of_numbers) // 2, -1):
    if sequence_of_numbers[idx] == 0:
        right_car_time = right_car_time * 0.8

    right_car_time += sequence_of_numbers[idx]

if left_car_time < right_car_time:
    print(f"The winner is left with total time: {left_car_time:.1f}")
else:
    print(f"The winner is right with total time: {right_car_time:.1f}")
