data = input()

phonebook = {}

while "-" in data:
    name, phone_number = data.split("-")
    phonebook[name] = phone_number
    data = input()

data = int(data)
for _ in range(data):
    person_name = input()
    if person_name in phonebook:
        print(f"{person_name} -> {phonebook[person_name]}")
    else:
        print(f"Contact {person_name} does not exist.")

