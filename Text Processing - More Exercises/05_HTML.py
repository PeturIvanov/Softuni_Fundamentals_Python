title = input()
print(f"<h1>\n{' ' * 4}{title}\n</h1>")
content = input()
print(f"<article>\n{' ' * 4}{content}\n</article>")
comments = input()
while comments != "end of comments":
    print(f"<div>\n{' ' * 4}{comments}\n</div>")
    comments = input()
