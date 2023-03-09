keys = int(input())

words = {}

for _ in range(keys):
    key = input()
    synonym = input()
    if key not in words:
        words[key] = []
    words[key].append(synonym)


for word, synonyms in words.items():
    print(f"{word} - {', '.join(synonyms)}")

