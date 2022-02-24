number_el = int(input())
train_list = []
for el in range(number_el):
    train_list.append(0)
index = 0
comand = input().split(" ")
while not comand[0] == "End":
    if comand[0] == "add":
        index = int(comand[1])
        train_list[-1] += int(comand[1])
    if comand[0] == "leave":
        index = int(comand[1])
        train_list[index] -= int(comand[2])
    if comand[0] == "insert":
        index = int(comand[1])
        train_list[index] += int(comand[2])
    comand = input().split(" ")
if comand[0] == "End":
    print(train_list)