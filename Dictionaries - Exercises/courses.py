courses_information = {}

command = input()

while command != "end":
    course_name, student_name = command.split(" : ")

    if course_name not in courses_information:
        courses_information[course_name] = []

    courses_information[course_name].append(student_name)

    command = input()

for courses, students in courses_information.items():
    print(f"{courses}: {len(students)}")
    for name in students:
        print(f"-- {name}")
