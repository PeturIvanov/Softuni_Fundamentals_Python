quantity_of_decorations_per_day = int(input())
days_left = int(input())

ornament_set_points = 5
tree_skirt_points = 3
tree_garland_points = 10
tree_lights_points = 17

quantity = quantity_of_decorations_per_day

total_cost = 0
total_spirit_points = 0

for day in range(1, days_left + 1):
    if day % 11 == 0:
        quantity += 2

    if day % 2 == 0:
        total_cost += 2 * quantity
        total_spirit_points += ornament_set_points
    if day % 3 == 0:
        total_cost += ((5 + 3) * quantity)
        total_spirit_points += (tree_skirt_points + tree_garland_points)
    if day % 5 == 0:
        total_cost += (15 * quantity)
        total_spirit_points += tree_lights_points
        if day % 3 == 0:
            total_spirit_points += 30

    if day % 10 == 0:
        total_spirit_points -= 20
        total_cost += (5 + 3 + 15)

if days_left % 10 == 0:
    total_spirit_points -= 30

print(f'Total cost: {total_cost}')
print(f'Total spirit: {total_spirit_points}')
