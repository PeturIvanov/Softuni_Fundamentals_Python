import re

text = input().lower()
word = input().lower()
pattern = rf"(^|(?<= )){word}($|(?=\W))"
result = re.finditer(pattern, text)
word_counter = []
for res in result:
    word_counter.append(res.group())
print(len(word_counter))

# import re
# text = input()
# searched_word = input()
#
# pattern = rf"\b{searched_word}\b"
# count_words = re.findall(pattern,text, re.IGNORECASE)
# print(len(count_words))
