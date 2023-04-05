import re

pattern = r"\+359\-2\-\d{3}\-\d{4}\b|\+359 2 \d{3} \d{4}\b"

numbers = input()

result = re.findall(pattern, numbers)
print(*result, sep=", ")