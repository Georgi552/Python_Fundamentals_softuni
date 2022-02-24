list = input().split(", ")
int_list = [int(el) for el in list]
index = 10
current_list = []
while len(int_list) > 0:
    for el in int_list:
        if el <= index:
            current_list.append(el)
    for el in current_list:
        if el == el in int_list:
            int_list.remove(el)

    print(f"Group of {index}'s: {current_list}")
    current_list = []
    index += 10
