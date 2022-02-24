products = {}
comand = input()
while not comand == "statistics":
    new_el = comand.split(": ")
    product = new_el[0]  # Key
    quantity = int(new_el[1])  # Value
    if product not in products.keys():
        products[product] = 0
    products[product] += quantity

    comand = input()

if comand == "statistics":
    print(f"Products in stock:")
    for key, value in products.items():
        print(f"- {key}: {value}")
    print(f"Total Products: {len(products.keys())}")
    print(f"Total Quantity: {sum(products.values())}")