def removing_pokemon(idx, pokemons):
    if 0 <= idx < len(pokemons):
        captures_pokemons.append(pokemons[idx])
        pokemons.pop(idx)
    elif idx < 0:
        captures_pokemons.append(pokemons[0])
        pokemons.pop(0)
        pokemons.insert(0, pokemons[-1])
    elif idx > len(pokemons) - 1:
        captures_pokemons.append(pokemons[-1])
        del pokemons[-1]
        pokemons.insert(len(pokemons), pokemons[0])

    for i, n in enumerate(pokemons):
        if n <= captures_pokemons[-1]:
            pokemons[i] += captures_pokemons[-1]
        elif n > captures_pokemons[-1]:
            pokemons[i] -= captures_pokemons[-1]


pokemon_inp = [int(x) for x in input().split()]
captures_pokemons = []

while len(pokemon_inp) > 0:
    index = int(input())
    removing_pokemon(index, pokemon_inp)

print(sum(captures_pokemons))