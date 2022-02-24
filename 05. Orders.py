products = input().split(" ")

dic_products = {}

while not products[0] == "buy":
    item = products[0]
    price = float(products[1])
    quantity = float(products[2])
    if item not in dic_products:
        dic_products[item] = [price, quantity]
    elif item in dic_products.keys():
        for el, mel in dic_products.items():
            if el == item:
                mel[0] = price
                mel[1] += quantity


    products = input().split(" ")

if products[0] == "buy":
    dic_products_total = {}
    for key, value in dic_products.items():
        dic_products_total[key] = (value[0] * value[1])

    for key, value in dic_products_total.items():
        print(f"{key} -> {value :.2f}")