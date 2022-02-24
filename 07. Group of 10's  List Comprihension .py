list = input().split(", ")
int_list = [int(el) for el in list]
index = 10
current_list = []
while len(int_list) > 0:
    current_list = [el for el in int_list if el <= index]

    int_list = [el for el in int_list if not el == el in current_list]


    print(f"Group of {index}'s: {current_list}")
    current_list = []
    index += 10
