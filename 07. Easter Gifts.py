gifts = str(input())
gifts_list = gifts.split(" ")

current_list = []

comand = input()
while comand != "No Money":
    comand_list = comand.split(" ")
    if comand_list[0] == "OutOfStock":
        for i in range(len(gifts_list)):
            if comand_list[1] == gifts_list[i]:
                current_list.append("None")
            else:
                current_list.append(gifts_list[i])

    if comand_list[0] == "Required":
            for i in range(len(gifts_list)):
                if i < int(comand_list[2]):
                    current_list.append(gifts_list[i])
                if i == int(comand_list[2]):
                    current_list.append(comand_list[1])
                if i > int(comand_list[2]):
                    current_list.append(gifts_list[i])


    if comand_list[0] == "JustInCase":
        for i in range(len(gifts_list) - 1):
            current_list.append(gifts_list[i])
        current_list.append(comand_list[1])

    gifts_list = current_list
    current_list = []
    comand = input()

if comand == "No Money":
    current_list = gifts_list
    for element in gifts_list:
        if element == "None":
            gifts_list.remove(element)


print(" ".join(gifts_list))