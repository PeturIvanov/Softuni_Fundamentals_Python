# word = input()
# new_word = ""
# for letter in word:
#     if letter.lower() not in ["a", "o", "u", "e", "i"]:
#         new_word += letter
#
#
# print(new_word)
#
# list comprehension:

word = input()
new_word = [i for i in word if i.lower() not in ["a", "o", "u", "e", "i"]]
print("".join(new_word))


