list_of_names = input().split(", ")

# sort by, then by
sorted_list = sorted(list_of_names, key=lambda x: (-len(x), x))

print(sorted_list)