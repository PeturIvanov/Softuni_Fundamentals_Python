cards = input()

team_a_count = 11
team_b_count = 11

my_list = cards.split()
clear_list = []
for duplicates in my_list:
    if duplicates not in clear_list:
        clear_list.append(duplicates)

for el in clear_list:
    if el[0] == "A":
        team_a_count -= 1

    elif el[0] == "B":
        team_b_count -= 1

    if team_a_count < 7 or team_b_count < 7:
        print(f"Team A - {team_a_count}; Team B - {team_b_count}")
        print("Game was terminated")
        exit()

print(f"Team A - {team_a_count}; Team B - {team_b_count}")
