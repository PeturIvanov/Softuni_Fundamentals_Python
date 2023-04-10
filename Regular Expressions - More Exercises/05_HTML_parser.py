import re

html_text = input().replace(r"\n", "")
pattern_title = r"(?:<title>)(?P<title>.+)(?:</title>)"
pattern_content = r"(?:<body>)(?P<content>.+)(?:</body>)"

title_text = re.search(pattern_title, html_text).group("title")
content_text = re.search(pattern_content, html_text).group("content")

replace_pattern = r"<.*?>"
title_text = re.sub(replace_pattern, "", title_text)
content_text = re.sub(replace_pattern, "", content_text)

print(f"Title: {title_text}")
print(f"Content: {content_text}")
