list = input().split("|")
comand = input()
while not comand == "Shop!":
    list_comand = comand.split("%")
    if list_comand[0] == "Important":
        if list_comand[1] in list:
            list.remove(list_comand[1])
            list.insert(0, list_comand[1])
        if list_comand[1] not in list:
            list.insert(0, list_comand[1])
    if list_comand[0] == "Add":
        if list_comand[1] not in list:
            list.append(list_comand[1])
        else:
            print(f"The product is already in the list.")
    if list_comand[0] == "Swap":
        if list_comand[1] in list and list_comand[2] in list:
            index1 = 0
            index2 = 0
            for i in range(len(list)):
                if list[i] == list_comand[1]:
                    index1 = i
            for i in range(len(list)):
                if list[i] == list_comand[2]:
                    index2 = i

            list[index1], list[index2] = list[index2], list[index1]

        if list_comand[1] not in list:
            print(f"Product {list_comand[1]} missing!")
        if list_comand[2] not in list:
            print(f"Product {list_comand[2]} missing!")
    if list_comand[0] == "Remove":
        if list_comand[1] in list:
            list.remove(list_comand[1])
        else:
            print(f"Product {list_comand[1]} isn't in the list.")
    if list_comand[0] == "reversed":
        list.reverse()
    comand = input()

if comand == "Shop!":
    for i in range(len(list)):
        print(f"{i + 1}. {list[i]}")
