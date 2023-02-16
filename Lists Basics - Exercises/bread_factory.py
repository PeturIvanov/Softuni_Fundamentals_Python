events = input().split("|")

init_coins = 100
energy = 100
gained_energy = 0

flag = True

for el in events:
    event = el.split("-")
    event_name = event[0]
    event_value = int(event[1])

    if event_name == "rest":
        energy += event_value
        if energy > 100:
            unused_energy = energy - 100
            gained_energy = event_value - unused_energy
            energy = 100
        else:
            gained_energy += event_value

        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {energy}.")
    elif event_name == "order":
        if energy >= 30:
            print(f"You earned {event_value} coins.")
            init_coins += event_value
            energy -= 30
        else:
            energy += 50
            print("You had to rest!")
    else:
        if event_value <= init_coins:
            print(f"You bought {event_name}.")
            init_coins -= event_value
        else:
            print(f"Closed! Cannot afford {event_name}.")
            flag = False
            break

if flag:
    print("Day completed!")
    print(f"Coins: {init_coins}")
    print(f"Energy: {energy}")
