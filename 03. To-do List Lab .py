list_to_do = [0] * 10
index = 0
to_dos = input().split("-")
while not to_dos[0] == "End":
    index = int(to_dos[0]) - 1
    list_to_do.pop(index)
    list_to_do.insert(index, to_dos[1])
    to_dos = input().split("-")

print([el for el in list_to_do if not el == 0])