number_of_electrons = int(input())

shells = []
while number_of_electrons > 0:
    shells.append(0)

    if number_of_electrons < 2 * ((shells.index(0) + 1) ** 2):

        shells[shells.index(0)] += number_of_electrons
        number_of_electrons -= number_of_electrons

    else:
        number_of_electrons -= 2 * ((shells.index(0) + 1) ** 2)
        shells[shells.index(0)] += 2 * ((shells.index(0) + 1) ** 2)


print(shells)
