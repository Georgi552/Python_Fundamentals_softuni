comand = input()

while not comand == "end":
    comand = str(comand)
    reverse = comand[::-1]
    print(f"{comand} = {reverse}")
    comand = input()

