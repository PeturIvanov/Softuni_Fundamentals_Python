user_data = input()

contests_info = {}

while user_data != "no more time":
    username, contest, points = user_data.split(" -> ")
    points = int(points)

    if contest not in contests_info:
        contests_info[contest] = {username: points}
    else:
        if username not in contests_info[contest]:
            contests_info[contest][username] = points
        else:
            if points > contests_info[contest][username]:
                contests_info[contest][username] = points
    user_data = input()

for contest in contests_info:
    contests_info[contest] = dict(sorted(contests_info[contest].items(), key=lambda x: (-x[1], x[0])))

counter = 1
for contest, students_names in contests_info.items():
    print(f"{contest}: {len(students_names.keys())} participants")
    counter = 1
    for name, score in students_names.items():
        print(f"{counter}. {name} <::> {score}")
        counter += 1

individual_info = {}

for course, students_names in contests_info.items():
    for name, score in students_names.items():
        if name not in individual_info:
            individual_info[name] = 0
        individual_info[name] += score

individual_info = dict(sorted(individual_info.items(), key=lambda x: (-x[1], x[0])))

counter = 1
print("Individual standings:")
for name, total_score in individual_info.items():
    print(f"{counter}. {name} -> {total_score}")
    counter += 1
