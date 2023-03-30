import re
key_sequence = [int(x) for x in input().split()]

string_to_decrypt = input()

while string_to_decrypt != "find":
    decrypted_message = ""

    index = 0
    for char in string_to_decrypt:
        character_to_add = ord(char) - key_sequence[index]
        decrypted_message += chr(character_to_add)
        if index == len(key_sequence) - 1:
            index = 0
        else:
            index += 1

    # find type and coordinates with RegEx.
    type_of_treasure = re.search(r'&(.+?)&', decrypted_message).group(1)
    coordinates = re.search(r'<(.+?)>', decrypted_message).group(1)

    # find coordinates with slicing.
    # coordinates = decrypted_message[decrypted_message.index("<") + 1:decrypted_message.index(">")]

    print(f"Found {type_of_treasure} at {coordinates}")

    string_to_decrypt = input()