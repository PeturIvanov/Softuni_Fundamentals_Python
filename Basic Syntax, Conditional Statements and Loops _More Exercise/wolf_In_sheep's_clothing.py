animals = input()
queue = animals.split(", ")

index = len(queue) - 1

for char in queue:
    if index == 0 and char == "wolf":
        print(f"Please go away and stop eating my sheep")
    elif char == "wolf":
        print(f"Oi! Sheep number {index}! You are about to be eaten by a wolf!")

    index -= 1
