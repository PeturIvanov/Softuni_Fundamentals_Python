snowballs_count = int(input())

best_snowball = 0
snowballs_weight = 0
snowballs_speed = 0
snowballs_quality = 0

for data in range(1, snowballs_count + 1):
    weight = int(input())
    speed = int(input())
    quality = int(input())

    value = (weight / speed) ** quality
    if value > best_snowball:
        best_snowball = int(value)
        snowballs_weight = weight
        snowballs_speed = speed
        snowballs_quality = quality

print(f"{snowballs_weight} : {snowballs_speed} = {best_snowball} ({snowballs_quality})")



