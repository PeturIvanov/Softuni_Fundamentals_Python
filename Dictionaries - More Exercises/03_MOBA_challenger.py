players_info = {}

commands = input()

while commands != "Season end":
    if "vs" not in commands:
        player_name, position, skill_points = commands.split(" -> ")
        skill_points = int(skill_points)

        if player_name not in players_info:
            players_info[player_name] = {position: skill_points}

        else:
            if position not in players_info[player_name]:
                players_info[player_name][position] = skill_points
            else:
                if skill_points > players_info[player_name][position]:
                    players_info[player_name][position] = skill_points
    else:
        player_one, player_two = commands.split(" vs ")

        flag = False
        fight_position = ""
        if player_one in players_info and player_two in players_info:
            player_one_positions = players_info[player_one].keys()
            player_two_positions = players_info[player_two].keys()
            for position in player_one_positions:
                if position in player_two_positions:
                    fight_position = position
                    flag = True

        if flag:
            player_one_skill_points = players_info[player_one][fight_position]
            player_two_skill_points = players_info[player_two][fight_position]

            if player_one_skill_points > player_two_skill_points:
                players_info.pop(player_two)
            elif player_two_skill_points > player_one_skill_points:
                players_info.pop(player_one)

    commands = input()

print(players_info)
top_players = {}

for player in players_info:
    top_players[player] = sum(players_info[player].values())

top_players = dict(sorted(top_players.items(), key=lambda x: (-x[1], x[0])))

for player in players_info:
    players_info[player] = dict(sorted(players_info[player].items(), key=lambda x: (-x[1], x[0])))

for player, total_skill in top_players.items():
    print(f"{player}: {total_skill} skill")
    for position, skill in players_info[player].items():
        print(f"- {position} <::> {skill}")
