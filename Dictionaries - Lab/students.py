data = input()
courses = {}

while ":" in data:
    student_name, student_id, course_name = data.split(":")
    if course_name not in courses:
        courses[course_name] = {student_id: student_name}
    else:
        courses[course_name][student_id] = student_name
    data = input()

data = data.replace("_", " ")
course = courses[data]

for student_id, name in course.items():
    print(f"{name} - {student_id}")
