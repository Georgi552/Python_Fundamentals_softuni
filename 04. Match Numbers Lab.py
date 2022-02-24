import re
names = input()
pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = re.finditer(pattern, names)
dates = [num.group() for num in matches]
print(*dates)
