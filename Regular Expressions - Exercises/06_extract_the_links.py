import re

text = input()
pattern = r"w{3}\.{1}(?P<domain_name>[A-Za-z\d\-]+)(\.[a-z]{1}[a-z\d]+){1,}"

while text:
    links = re.finditer(pattern, text)
    for link in links:
        print(link.group())
    text = input()