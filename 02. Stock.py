list = input().split(" ")
spisyuk = input().split(" ")
products = {}
for index in range(len(list)):
    if not index % 2 == 0:
        key = (list[index - 1])
        values = (int(list[index]))
        products[key] = values

for el in spisyuk:
    if el in products:
        print(f"We have {products[el]} of {el} left")
    else:
        print(f"Sorry, we don't have {el}")