import re

input_lines = int(input())

for data in range(input_lines):
    string = input()

    # name = string[string.index("@") + 1:string.index("|")]
    # age = string[string.index("#") + 1:string.index("*")]
    # print(f"{name} is {age} years old.")

    name = re.search(r'@(.+?)\|', string).group(1)
    age = re.search(r'#(\d+)\*', string).group(1)
    print(f"{name} is {age} years old.")

