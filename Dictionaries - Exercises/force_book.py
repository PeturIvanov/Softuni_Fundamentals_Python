factions = {}
database = []
commands = input()

while commands != "Lumpawaroo":
    if "|" in commands:
        faction, user_name = commands.split(" | ")

        if user_name not in database:
            if faction not in factions:
                factions[faction] = []
                factions[faction].append(user_name)
                database.append(user_name)
            else:
                factions[faction].append(user_name)
                database.append(user_name)

    elif "->" in commands:
        user_name, faction = commands.split(" -> ")

        if user_name in database:
            for faction_key, members in factions.items():
                if user_name in members:
                    members.remove(user_name)

            if faction not in factions:
                factions[faction] = []
                factions[faction].append(user_name)
            else:
                factions[faction].append(user_name)

        elif user_name not in database and faction in factions:
            factions[faction].append(user_name)
            database.append(user_name)

        elif user_name not in database and faction not in factions:
            factions[faction] = []
            factions[faction].append(user_name)
            database.append(user_name)

        print(f"{user_name} joins the {faction} side!")

    commands = input()

factions = {faction: members for faction, members in factions.items() if members}

for faction, members in factions.items():
    print(f"Side: {faction}, Members: {len(members)}")
    for member in members:
        print(f"! {member}")
