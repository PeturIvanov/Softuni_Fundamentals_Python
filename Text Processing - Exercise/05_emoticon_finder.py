text = input()

for i, char in enumerate(text):
    emoji = ""
    if char == ":":
        emoji += (char + text[i + 1])
        print(emoji)