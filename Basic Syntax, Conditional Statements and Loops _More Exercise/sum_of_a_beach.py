word = input().lower()
words_to_find = ["water", "fish", "sun", "sand"]
counter = 0
counter += word.count("sun")
counter += word.count("fish")
counter += word.count("sand")
counter += word.count("water")
print(counter)
