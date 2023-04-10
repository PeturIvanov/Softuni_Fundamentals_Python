import re

pattern = r"[\-]?[\d]*[\.]?[\d]+"
pattern_regex = re.compile(pattern)

string = input()

list_of_demons = string.replace(',', ' ').split()
list_of_demons = sorted(list_of_demons)
demons_info = {}

for demon in list_of_demons:
    demons_info[demon] = {"health": 0, "damage": 0}

for demon in list_of_demons:
    demon_health = 0
    for char in demon:
        if not char.isdigit() and char not in ["+", "-", "*", "/", "."]:
            demon_health += ord(char)

    demons_info[demon]["health"] = demon_health

for demon in list_of_demons:
    digits = re.findall(pattern_regex, demon)
    digits = [float(x) for x in digits]
    demon_damage = sum(digits)
    for char in demon:
        if char == "/":
            demon_damage = demon_damage / 2
        elif char == "*":
            demon_damage *= 2
    demons_info[demon]["damage"] = demon_damage


for name in demons_info:
    print(f"{name} - {demons_info[name]['health']} health, {demons_info[name]['damage']:.2f} damage")


