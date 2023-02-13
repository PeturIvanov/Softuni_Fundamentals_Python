lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_sum = 0
shield_brake = 0
for lost in range(1, lost_fights_count + 1):
    if lost % 2 == 0:
        total_sum += helmet_price

    if lost % 3 == 0:
        total_sum += sword_price

    if lost % 3 == 0 and lost % 2 == 0:
        total_sum += shield_price
        shield_brake += 1

    if shield_brake % 2 == 0 and shield_brake > 0:
        total_sum += armor_price
        shield_brake = 0


print(f"Gladiator expenses: {total_sum:.2f} aureus")
