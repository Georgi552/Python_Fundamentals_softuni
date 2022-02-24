items = input().split(", ")
comand = str(input())
while not comand == "Craft!":
    comanda = comand.split(" - ")
    if comanda[0] == "Collect":
        if comanda[1] not in items:
            items.append(comanda[1])
        if comanda[1] in items:
            pass

    if comanda[0] == "Drop":
        if comanda[1] in items:
            items.remove(comanda[1])
        else:
            pass
    if comanda[0] == "Combine Items":
        index = comanda[1].split(":")
        for i in range(len(items)):
            if items[i] == index[0]:
                items.insert((i + 1), index[1])

    if comanda[0] == "Renew":
        if comanda[1] in items:
            items.remove(comanda[1])
            items.append(comanda[1])
    comand = str(input())
if comand == "Craft!":
    print(", ".join(items))