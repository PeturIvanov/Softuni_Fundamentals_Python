dragons_count = int(input())
dragons_data = {}

for _ in range(1, dragons_count + 1):
    dragon_type, dragon_name, damage, health, armor = [int(el) if el.isdigit() else el for el in input().split()]
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    if dragon_type not in dragons_data:
        dragons_data[dragon_type] = {dragon_name: [damage, health, armor]}

    else:
        if dragon_name not in dragons_data[dragon_type]:
            dragons_data[dragon_type][dragon_name] = [damage, health, armor]
        else:
            dragons_data[dragon_type][dragon_name] = [damage, health, armor]


for types in dragons_data:
    dragons_data[types] = dict(sorted(dragons_data[types].items(), key=lambda x: x[0]))

for types in dragons_data:
    damage_total_stats, health_total_stats, armor_total_stats = 0, 0, 0

    for stats in dragons_data[types].values():
        damage_total_stats += stats[0]
        health_total_stats += stats[1]
        armor_total_stats += stats[2]

    average_damage = damage_total_stats / len(dragons_data[types])
    average_health = health_total_stats / len(dragons_data[types])
    average_armor = armor_total_stats / len(dragons_data[types])

    print(f"{types}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for name, stats in dragons_data[types].items():
        print(f"-{name} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")
