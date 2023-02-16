fires = input().split("#")
amount_water = int(input())

total_water_left = amount_water
total_effort = 0
total_fire = 0
print("Cells:")
for el in fires:
    type_of_fire = el.split(" = ")
    cell_value = int(type_of_fire[1])

    if type_of_fire[0] == "High" and (cell_value < 81 or cell_value > 125):
        continue
    elif type_of_fire[0] == "Medium" and (cell_value < 51 or cell_value > 80):
        continue
    elif type_of_fire[0] == "Low" and (cell_value < 1 or cell_value > 50):
        continue

    if cell_value <= total_water_left:
        total_water_left -= cell_value
        total_effort += cell_value * 0.25
        total_fire += cell_value
    else:
        continue

    print(f" - {cell_value}")

print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")
