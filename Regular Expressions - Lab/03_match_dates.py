import re

pattern = r"\b(?P<Day>\d{2})(\.|\-|/)(?P<Month>[A-Z][a-z]{2})\2(?P<Year>\d{4})\b"

text = input()

dates = re.finditer(pattern, text)

for date in dates:
    current_date = date.groupdict()
    print(f"Day: {current_date['Day']}, Month: {current_date['Month']}, Year: {current_date['Year']}")
