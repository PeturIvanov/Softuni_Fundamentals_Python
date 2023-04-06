import re

pattern = r"(^|(?<= ))_(?P<name>([A-Za-z0-9]+))\b"
text = input()
valid_names = re.finditer(pattern, text)
names = []

for name in valid_names:
    names.append(name.group("name"))

print(*names, sep=",")
