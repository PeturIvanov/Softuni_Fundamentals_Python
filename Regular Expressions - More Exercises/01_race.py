names_list = input().split(", ")

data = input()
racers_info = {}
for name in names_list:
    racers_info[name] = 0

while data != "end of race":
    name = ""
    distance_km = 0
    for char in data:
        if char.isalpha():
            name += char
        if char.isdigit():
            distance_km += int(char)

    if name in names_list:
        racers_info[name] += distance_km
    data = input()

racers_info = dict(sorted(racers_info.items(), key=lambda x: -x[1]))

for i, name in enumerate(racers_info.keys(), 1):
    sub_text = ""
    if i == 1:
        sub_text = "st"
    elif i == 2:
        sub_text = "nd"
    elif i == 3:
        sub_text = "rd"
    else:
        exit(0)

    print(f"{i}{sub_text} place: {name}")

