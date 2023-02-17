numbers = input().split()
message = input()
new_word = []
for sequence in numbers:
    current_sum = 0
    for index in sequence:
        current_sum += int(index)

    current_sum = current_sum % len(message)
    new_word.append(message[current_sum])
    message = message.replace(message[current_sum], "", 1)
print(*new_word, sep="")
