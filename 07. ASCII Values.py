list = input().split(", ")

dict = {}

for el in list:
    dict[el] = ord(el)
print(dict)