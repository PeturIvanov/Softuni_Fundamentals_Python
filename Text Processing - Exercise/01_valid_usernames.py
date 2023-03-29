usernames = input().split(", ")

for username in usernames:
    flag = True
    if 3 < len(username) <= 16:
        for char in username:
            if not char.isdigit() and not char.isalpha() and char != "-" and char != "_" or char == " ":
                flag = False
                break
    else:
        continue
    if flag:
        print(username)
