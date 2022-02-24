work = input()
work_list = work.split("|")

coins = 100
energy = 100
number = 0
breaking = 0
for i in range(len(work_list)):
    work_day = work_list[i].split("-")
    if work_day[0] == "rest":
        number = int(work_day[1])
        if energy < 100:
            if energy + number <= 100:
                energy += number
            if energy + number > 100:
                number = 100 - energy
                energy += number
        if energy == 100:
            print("You gained 0 energy.")
            print(f"Current energy: {energy}.")
            continue

        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")

    if work_day[0] == "order":
        number = int(work_day[1])
        if energy >= 30:
            energy -= 30
            coins += number
            print(f"You earned {number} coins.")
        elif energy < 30:
            energy += 50
            print("You had to rest!")

    if work_day[0] != "order" and work_day[0] != "rest":
        number = int(work_day[1])
        if coins > number:
            coins -= number
            print(f"You bought {work_day[0]}.")
            number = 0
        if coins <= number:
            print(f"Closed! Cannot afford {work_day[0]}.")
            breaking += 1
            break
if breaking == 0:

    print(f"Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")
else:
    pass
