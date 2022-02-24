import re
names = input()
regex = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})"
matches = re.finditer(regex, names)
valid_phones = [match.group() for match in matches]
print(", ".join(valid_phones))