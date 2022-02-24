clothes_list = input().split("|")
money = float(input())
profit = 0
total_money = money
profit_list = []
for i in range(len(clothes_list)):
    current_list = clothes_list[i]
    test_list = current_list.split("->")
    index = float(test_list[1])
    if test_list[0] == "Clothes":
        if index <= 50.00 and index <= money:
            money -= index
            profit += index * 0.40
            total_money += index * 0.40
            profit_list.append(index * 1.40)
        else:
            pass
    if test_list[0] == "Shoes":
        if index <= 35.00 and index <= money:
            money -= index
            profit += index * 0.40
            total_money += index * 0.40
            profit_list.append(index * 1.40)
        else:
            pass
    if test_list[0] == "Accessories":
        if index <= 20.50 and index <= money:
            money -= index
            profit += index * 0.40
            total_money += index * 0.40
            profit_list.append(index * 1.40)
        else:
            pass


for i in range(len(profit_list)):
    profit_list[i] = float(profit_list[i])

formatted_list = []
for item in profit_list:
    formatted_list.append("%.2f"%item)
print(" ".join(formatted_list))
print(f"Profit: {profit :.2f}")
if total_money >= 150:
    print(f"Hello, France!")
else:
    print("Time to go.")