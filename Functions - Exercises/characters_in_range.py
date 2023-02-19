def ascci_characters(start, end):
    start_index = ord(start)
    end_index = ord(end)
    for char in range(start_index + 1, end_index):
        print(chr(char), end=" ")


start_char = input()
end_char = input()

ascci_characters(start_char, end_char)
