import re

txt = input().lower()
search_word = input().lower()
x = re.findall(rf'\b{search_word}\b', txt)

print(len(x))

