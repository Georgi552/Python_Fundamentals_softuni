fires_list = input().split("#")
water = int(input())

current_list = []
effort = 0
total_fire = 0
print("Cells:")
for i in range(len(fires_list)):
    current_list = fires_list[i]
    test_list = current_list.split(" = ")
    index = int(test_list[1])

    if test_list[0] == "Low":
        if 1 <= index <= 50:
            if water >= index:
                water -= index
                effort += index * 0.25
                total_fire += index
                print(f"- {index}")
            else:
                pass
        else:
            pass

    if test_list[0] == "Medium":
        if 51 <= index <= 80:
            if water >= index:
                water -= index
                effort += index * 0.25
                total_fire += index
                print(f"- {index}")
            else:
                pass
        else:
            pass

    if test_list[0] == "High":
        if 81 <= index <= 125:
            if water >= index:
                water -= index
                effort += index * 0.25
                total_fire += index
                print(f"- {index}")
            else:
                pass
        else:
            pass
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
