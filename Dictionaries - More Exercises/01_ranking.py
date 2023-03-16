contests_data = input()
contests = {}

while contests_data != "end of contests":
    contest, password = contests_data.split(":")
    contests[contest] = password
    contests_data = input()

submissions_data = input()
submissions = {}

while submissions_data != "end of submissions":
    contest, password, username, points = submissions_data.split("=>")
    points = int(points)

    # if contest in contests and password == contests[contest]:
    #     if username not in submissions:
    #         submissions[username] = {contest: points}
    #     elif username in submissions:
    #         if contest not in submissions[username]:
    #             submissions[username][contest] = points
    #         else:
    #             if points > submissions[username][contest]:
    #                 submissions[username][contest] = points

    if contest in contests and password in contests[contest]:
        submissions[username] = submissions.get(username, {})
        submissions[username][contest] = submissions[username].get(contest, 0)
        if submissions[username][contest] < points:
            submissions[username][contest] = points
    submissions_data = input()

candidates_total_score = {}

for candidate, course in submissions.items():
    candidates_total_score[candidate] = 0
    for score in course.values():
        candidates_total_score[candidate] += score

best_candidate = ""
best_score = 0
for candidate, total_score in candidates_total_score.items():
    if total_score > best_score:
        best_score = total_score
        best_candidate = candidate

print(f"Best candidate is {best_candidate} with total {best_score} points.")
print("Ranking:")
submissions = dict(sorted(submissions.items(), key=lambda item: item[0]))
for name in submissions:
    submissions[name] = dict(sorted(submissions[name].items(), key=lambda x: -x[1]))
    print(name)
    for contest, points in submissions[name].items():
        print(f"#  {contest} -> {points}")
