import re


lines = []
while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break
names = '\n'.join(lines)

pattern = r"\d+"
matches = re.findall(pattern, names)
print(*matches, end=" ")
    #print("".join(matches), end=" "
