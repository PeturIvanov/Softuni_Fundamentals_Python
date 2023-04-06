import re

pattern = r"(^|(?<= ))[a-z\d]{1}[a-z\d\.\_\-]*[a-z0-9$]\@[a-z\d]{1}[a-z\d\-]+[a-z\d$][\.][a-z\d]{1}[a-z\d\.\-]*[a-z\d$]"
text = input()

emails = re.finditer(pattern, text)

for email in emails:
    print(email.group())