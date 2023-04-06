import re

pattern = r"\d+"
current_text = input()

while current_text:
    digits = re.finditer(pattern, current_text)
    for digit in digits:
        print(digit.group(), end=" ")
    current_text = input()


