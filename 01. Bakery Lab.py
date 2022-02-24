list = input().split(" ")
keys = []
values = []
for index in range(len(list)):
    if index % 2 == 0:
        keys.append(list[index])
    if not index % 2 == 0:
        values.append(int(list[index]))

print(dict(zip(keys, values)))
