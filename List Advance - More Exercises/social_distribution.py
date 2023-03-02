def richest_person(population_list):
    richest = 0
    for n in population_list:
        if n > richest:
            richest = n

    return richest


population = [int(x) for x in input().split(", ")]
wealth = int(input())
flag = True
for i, num in enumerate(population):
    current_richest = richest_person(population)

    if num <= wealth:
        diff = wealth - num
        if current_richest - diff >= wealth:
            index_richest = population.index(current_richest)
            population[index_richest] -= diff
            population[i] = wealth
        else:
            print(f"No equal distribution possible")
            flag = False
            break

if flag:
    print(population)
