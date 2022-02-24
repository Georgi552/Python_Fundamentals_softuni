n = int(input())
word = str(input())

text_list = []
for c in range(n):
    text = str(input())
    text_list.append(text)
print(text_list)

for s in range(len(text_list) -1, -1 , -1):
    element = text_list[s]
    if word not in element:
        text_list.remove(element)
print(text_list)
