employees_happiness = [int(n) for n in input().split()]
factor = int(input())

upgrade_happiness = [num * factor for num in employees_happiness]
average_happiness = sum(upgrade_happiness) / len(upgrade_happiness)
are_happy = 0
not_happy = 0
for num in upgrade_happiness:
    if num >= average_happiness:
        are_happy += 1
    else:
        not_happy += 1

if are_happy >= not_happy:
    print(f"Score: {are_happy}/{len(employees_happiness)}. Employees are happy!")
else:
    print(f"Score: {are_happy}/{len(employees_happiness)}. Employees are not happy!")
