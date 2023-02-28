def add(lesson_1):
    if lesson_1 not in schedule:
        schedule.append(lesson_1)


def insert(lesson_1, idx):
    if lesson_1 not in schedule:
        schedule.insert(idx, lesson_1)


def remove(lesson_1):
    if lesson_1 in schedule:
        schedule.remove(lesson_1)
    exercise_lesson = f"{lesson_1}-Exercise"
    if exercise_lesson in schedule:
        schedule.remove(exercise_lesson)


def swap(lesson_1, lesson_2):
    if lesson_1 in schedule and lesson_2 in schedule:
        lesson_1_idx = schedule.index(lesson_1)
        lesson_2_idx = schedule.index(lesson_2)
        schedule[lesson_1_idx], schedule[lesson_2_idx] = schedule[lesson_2_idx], schedule[lesson_1_idx]

        exercise_lesson_1 = f"{lesson_1}-Exercise"
        exercise_lesson_2 = f"{lesson_2}-Exercise"

        if exercise_lesson_2 in schedule:
            schedule.remove(exercise_lesson_2)
            schedule.insert(lesson_1_idx + 1, exercise_lesson_2)
        if exercise_lesson_1 in schedule:
            schedule.remove(exercise_lesson_1)
            schedule.insert(lesson_2_idx + 1, exercise_lesson_1)


def exercise(lesson_1):
    exercise_lesson = f"{lesson_1}-Exercise"
    if lesson_1 in schedule and exercise_lesson not in schedule:
        lesson_idx = schedule.index(lesson_1) + 1
        schedule.insert(lesson_idx, exercise_lesson)
    elif lesson_1 not in schedule:
        schedule.append(lesson_1)
        schedule.append(exercise_lesson)


schedule = input().split(", ")
commands = input()
while commands != "course start":
    data = commands.split(":")
    operator = data[0]
    lesson_title_1 = data[1]

    if operator == "Add":
        add(lesson_title_1)

    elif operator == "Insert":
        index = int(data[2])
        insert(lesson_title_1, index)
    elif operator == "Remove":
        remove(lesson_title_1)
    elif operator == "Swap":
        lesson_title_2 = data[2]
        swap(lesson_title_1, lesson_title_2)
    elif operator == "Exercise":
        exercise(lesson_title_1)

    commands = input()

for i, el in enumerate(schedule, 1):
    print(f"{i}.{el}")


