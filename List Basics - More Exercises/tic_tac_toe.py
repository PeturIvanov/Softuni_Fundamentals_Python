first_row = input().split()
second_row = input().split()
third_row = input().split()

all_rows = first_row + second_row + third_row

if all_rows[0] == "2" and all_rows[1] == "2" and all_rows[2] == "2":
    print("Second player won")

elif all_rows[0] == "1" and all_rows[1] == "1" and all_rows[2] == "1":
    print("First player won")


elif all_rows[3] == "1" and all_rows[4] == "1" and all_rows[5] == "1":
    print("First player won")

elif all_rows[3] == "2" and all_rows[4] == "2" and all_rows[5] == "2":
    print("Second player won")


elif all_rows[6] == "1" and all_rows[7] == "1" and all_rows[8] == "1":
    print("First player won")

elif all_rows[6] == "2" and all_rows[7] == "2" and all_rows[8] == "2":
    print("Second player won")


elif all_rows[0] == "1" and all_rows[3] == "1" and all_rows[6] == "1":
    print("First player won")

elif all_rows[0] == "2" and all_rows[3] == "2" and all_rows[6] == "2":
    print("Second player won")


elif all_rows[1] == "1" and all_rows[4] == "1" and all_rows[7] == "1":
    print("First player won")

elif all_rows[1] == "2" and all_rows[4] == "2" and all_rows[7] == "2":
    print("Second player won")


elif all_rows[2] == "1" and all_rows[5] == "1" and all_rows[8] == "1":
    print("First player won")

elif all_rows[2] == "2" and all_rows[5] == "2" and all_rows[8] == "2":
    print("Second player won")


elif all_rows[0] == "1" and all_rows[4] == "1" and all_rows[8] == "1":
    print("First player won")

elif all_rows[0] == "2" and all_rows[4] == "2" and all_rows[8] == "2":
    print("Second player won")


elif all_rows[2] == "1" and all_rows[4] == "1" and all_rows[6] == "1":
    print("First player won")

elif all_rows[2] == "2" and all_rows[4] == "2" and all_rows[6] == "2":
    print("Second player won")


else:
    print("Draw!")

