smal_element = input().split(", ")
text = input().split(", ")

result = [el for el in smal_element for elem in text if el in elem]
new = []
for el in result:
    if not el in new:
        new.append(el)

print(new)