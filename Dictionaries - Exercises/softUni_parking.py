n = int(input())

users = {}

for _ in range(n):
    command = input().split()
    operator = command[0]
    username = command[1]
    if operator == "register":
        license_plate_number = command[2]
        if username not in users:
            users[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {license_plate_number}")

    elif operator == "unregister":
        if username not in users:
            print(f"ERROR: user {username} not found")
        else:
            del users[username]
            print(f"{username} unregistered successfully")

for name, plate in users.items():
    print(f"{name} => {plate}")
