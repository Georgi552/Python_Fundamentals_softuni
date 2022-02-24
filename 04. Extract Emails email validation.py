import re

txt = input().lower()

regex = r"\s([a-zA-Z0-9]+[a-zA-Z0-9\.\,\-\_]*\@[a-zA-Z]+[a-zA-Z\-]*(\.[a-zA-Z]+)+)\b"


matches = re.finditer(regex, txt)
for match in matches:
    print(match.group(0))