rooms_count = int(input())

flag = True
free_chairs = 0

for rooms in range(1, rooms_count + 1):
    input_data = input().split(" ")
    chairs = len(input_data[0])
    visitors = int(input_data[1])

    if chairs >= visitors:
        free_chairs += chairs - visitors

    else:
        needed_chairs = visitors - chairs
        print(f"{needed_chairs} more chairs needed in room {rooms}")
        flag = False

if flag:
    print(f"Game On, {free_chairs} free chairs left")
