commands = input()

dwarfs_data = {}
# dwarf_info = {"red": {"Simon": 50}, "yellow": {"Happy": 40, "Simon": 30}}
while commands != "Once upon a time":
    dwarf_name, dwarf_hat_color, dwarf_physics = commands.split(" <:> ")
    dwarf_physics = int(dwarf_physics)

    if dwarf_hat_color not in dwarfs_data:
        dwarfs_data[dwarf_hat_color] = {dwarf_name: dwarf_physics}

    else:
        if dwarf_name not in dwarfs_data[dwarf_hat_color]:
            dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics
        else:
            if dwarf_physics > dwarfs_data[dwarf_hat_color][dwarf_name]:
                dwarfs_data[dwarf_hat_color][dwarf_name] = dwarf_physics

    commands = input()

sorted_dwarfs = []

for hat in dwarfs_data:
    for name, physic in dwarfs_data[hat].items():
        sorted_dwarfs.append({'length': len(dwarfs_data[hat]), 'name': name, 'physic': physic, 'hat_color': hat})

for show_result in sorted(sorted_dwarfs, key=lambda item: (-item['physic'], -item['length'])):
    print(f"({show_result['hat_color']}) {show_result['name']} <-> {show_result['physic']}")




