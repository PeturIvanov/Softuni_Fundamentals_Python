# words = input().split()
# palindrome = input()
#
# palindrome_list = []
# palindrome_counter = 0
#
# for word in words:
#     if word[::-1] == word:
#         palindrome_list.append(word)
#
#     if word == palindrome:
#         palindrome_counter += 1
# print(palindrome_list)
# print(f"Found palindrome {palindrome_counter} times")

words = input().split()
palindrome = input()

palindrome_list = []
palindrome_counter = 0

for word in words:
    reversed_word = "".join(reversed(word))
    if reversed_word == word:
        palindrome_list.append(word)
    if word == palindrome:
        palindrome_counter += 1
print(palindrome_list)
print(f"Found palindrome {palindrome_counter} times")
