group_size = int(input())
adventure_days = int(input())

current_group = group_size
coins = 0

for days in range(1, adventure_days + 1):
    coins += 50

    if days % 10 == 0:
        current_group -= 2

    if days % 15 == 0:
        current_group += 5

    coins -= 2 * current_group

    if days % 3 == 0:
        coins -= 3 * current_group

    if days % 5 == 0:
        coins += 20 * current_group
        if days % 3 == 0:
            coins -= 2 * current_group

coins_per_com = coins // current_group
print(f"{current_group} companions received {coins_per_com} coins each.")
