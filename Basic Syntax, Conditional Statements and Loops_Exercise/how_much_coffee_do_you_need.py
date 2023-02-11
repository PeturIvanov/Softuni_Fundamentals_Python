total_cups_of_coffee = 0

while True:
    event = input()
    if event == "END":
        break

    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        total_cups_of_coffee += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        total_cups_of_coffee += 2

if total_cups_of_coffee <= 5:
    print(f"{total_cups_of_coffee}")
else:
    print("You need extra sleep")
    