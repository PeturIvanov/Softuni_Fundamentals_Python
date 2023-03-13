junk = {}
key_fragments = {
    "shards": 0,
    "fragments": 0,
    "motes": 0
}

legendary_items = {
    "shards": "Shadowmourne",
    "fragments": "Valanyr",
    "motes": "Dragonwrath"
}


flag = True
while flag:
    line = input().lower()
    list_of_materials = [el for el in line.split()]

    for i in range(0, len(list_of_materials), 2):
        material = list_of_materials[i + 1]
        quantity = int(list_of_materials[i])

        if material in key_fragments:
            key_fragments[material] += quantity
            if key_fragments[material] >= 250:
                key_fragments[material] -= 250
                print(f"{legendary_items[material]} obtained!")
                flag = False
                break
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity


for k, v in key_fragments.items():
    print(f"{k}: {v}")

for k, v in junk.items():
    print(f"{k}: {v}")
