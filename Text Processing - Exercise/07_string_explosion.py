text = input()

result = ""
explosion = 0
lenght = 0

while lenght < len(text):
    for i in range(len(text)):
        if not text[i] == ">" and explosion > 0:
            explosion -= 1
        elif text[i] == ">":
            explosion += int(text[i + 1])
            result += text[i]
        else:
            result += text[i]
        lenght += 1

print(result)