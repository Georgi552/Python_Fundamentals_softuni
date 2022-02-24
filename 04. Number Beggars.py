money_list_str = input().split(", ")
begars = int(input())
current_sum = 0
start = 0
sums_each_begar = []

for begar in range(begars):
    current_sum = 0
    for num in range(start, len(money_list_str), begars):
        current_sum += int(money_list_str[num])
    sums_each_begar.append(current_sum)
    start += 1

print(sums_each_begar)