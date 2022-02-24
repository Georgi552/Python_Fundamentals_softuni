parts = input().split("|")

comand = input()
while not comand == "Done":
    comand_list = comand.split(" ")
    if comand_list[0] == "Add":
        if 0 <= int(comand_list[2]) <= (len(parts) - 1):
            parts.insert(int(comand_list[2]), comand_list[1])
        if int(comand_list[2]) > len(parts):
            pass
    if comand_list[0] == "Remove":
        if 0 <= int(comand_list[1]) <= (len(parts) - 1):
            parts.pop(int(comand_list[1]))
        if int(comand_list[1]) > len(parts):
            pass
    if comand_list[0] == "Check":
        if comand_list[1] == "Even":
            for i in range(len(parts)):
                if i % 2 == 0:
                    print("".join(parts[i]) , end= " ")

        if comand_list[1] == "Odd":
            for i in range(len(parts)):
                if not i % 2 == 0:
                    print("".join(parts[i]) , end= " ")
        else:
            pass
        print()

    comand = input()
if comand == "Done":
    print(f"You crafted {''.join(parts)}!")