banned = input().split(", ")
txt = input()

for el in banned:
    while el in txt:
        txt = txt.replace(el, "*" * len(el))
print(txt)