student_result = {}
submissions = {}

data = input()

while data != "exam finished":
    if "banned" not in data:
        username, language, points = data.split("-")
        points = int(points)

        if language not in submissions:
            submissions[language] = 0

        submissions[language] += 1

        if language not in student_result:
            student_result[language] = {}
            student_result[language][username] = 0

        if username not in student_result[language]:
            student_result[language][username] = 0

        if points > student_result[language][username]:
            student_result[language][username] = points

    else:
        banned_name = data.split("-")[0]
        for language, name in student_result.items():
            if banned_name in name:
                student_result[language].pop(banned_name)

    data = input()

print("Results:")

for course in student_result.keys():
    for student, result in student_result[course].items():
        print(f"{student} | {result}")

print("Submissions:")
for language, count in submissions.items():
    print(f"{language} - {count}")



