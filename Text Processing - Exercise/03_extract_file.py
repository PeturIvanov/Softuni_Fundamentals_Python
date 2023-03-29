path = input().split(".")
extension = path[-1]
path.remove(extension)
name = path[0].split("\\")[-1]

print(f"File name: {name}\nFile extension: {extension}")
