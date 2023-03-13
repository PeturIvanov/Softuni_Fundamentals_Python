students_count = int(input())

students_grades = {}

excellent_students = {}

for grades in range(students_count):
    student_name = input()
    student_grade = float(input())

    if student_name not in students_grades:
        students_grades[student_name] = []

    students_grades[student_name].append(student_grade)

for name, grades in students_grades.items():
    average_grade = sum(grades) / len(grades)

    if average_grade >= 4.50:
        excellent_students[name] = average_grade

for name, grade in excellent_students.items():
    print(f"{name} -> {grade:.2f}")
