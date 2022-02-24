comand = input().split("|")
health = 100
bitcoins = 0
room = 0
for el in comand:
    com = el.split(" ")
    if com[0] == "potion":
        room += 1
        if health + int(com[1]) > 100:
            gained_health = 100 - health
            health = 100
            print(f"You healed for {gained_health} hp.")
            print(f"Current health: {health} hp.")
        if health + int(com[1]) <= 100:
            health += int(com[1])
            print(f"You healed for {com[1]} hp.")
            print(f"Current health: {health} hp.")
    elif com[0] == "chest":
        room += 1
        bitcoins += int(com[1])
        print(f"You found {com[1]} bitcoins.")
    else:
        room += 1
        health -= int(com[1])
        if health > 0:
            print(f"You slayed {com[0]}.")
        if health <= 0:
            print(f"You died! Killed by {com[0]}.")
            print(f"Best room: {room}")
            break
if health > 0:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
