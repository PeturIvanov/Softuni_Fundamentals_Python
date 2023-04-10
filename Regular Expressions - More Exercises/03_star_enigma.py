import re

number_of_messages = int(input())
key_letters = ["s", "t", "a", "r"]

decrypted_messages = []

for message in range(1, number_of_messages + 1):
    encrypted_messages = input()
    key_letters_count = 0
    for char in encrypted_messages:
        if char.lower() in key_letters:
            key_letters_count += 1

    decrypted_message = ""

    for char in encrypted_messages:
        decrypted_message += chr(ord(char) - key_letters_count)

    decrypted_messages.append(decrypted_message)

pattern = r"[\@](?P<planet_name>[A-Za-z]+)[^\@\-\!\:\>]*?[\:]" \
          r"(?P<planet_population>[1-9][0-9]*)[^\@\-\!\:\>]*?[\!]" \
          r"(?P<attack_type>[A|D])[\!][^\@\-\!\:\>]*?[\-][\>]" \
          r"(?P<soldier_count>[1-9][0-9]*)"
pattern_regex = re.compile(pattern)

missions = {"A": [],
            "D": []}

for msg in decrypted_messages:
    data = re.finditer(pattern_regex, msg)
    for info in data:
        attack_information = info.groupdict()
        missions[attack_information["attack_type"]].append(attack_information["planet_name"])


print(f"Attacked planets: {len(missions['A'])}")
for planet in sorted(missions["A"]):
    print(f"-> {planet}")
print(f"Destroyed planets: {len(missions['D'])}")
for planet in sorted(missions["D"]):
    print(f"-> {planet}")
















