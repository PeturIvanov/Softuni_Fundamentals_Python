class Zoo:
    __animals = 0

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self. birds = []

    def add_animal(self, species, animal):
        if species == "mammal":
            self.mammals.append(animal)
        elif species == "fish":
            self.fishes.append(animal)
        elif species == "bird":
            self.birds.append(animal)

        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {zoo.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {zoo.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result += f"Birds in {zoo.name}: {', '.join(self.birds)}"

        return f"{result}\nTotal animals: {Zoo.__animals}"


name_of_zoo = input()
rows = int(input())
zoo = Zoo(name_of_zoo)
for _ in range(rows):
    species, animal = input().split()
    zoo.add_animal(species, animal)

type_of_animals = input()

print(zoo.get_info(type_of_animals))
