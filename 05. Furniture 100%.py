import re

product = input()
list_products = []
total_price = 0
while not product == "Purchase":
    pattern = r"([\$%])(?P<word>[A-Za-z])+(\1):\s\[(?P<simb1>\d+)\]\|\[(?P<simb2>\d+)\]\|\[(?P<simb3>\d+)\]\|"
    matches = re.finditer(pattern, product)
    for el in matches:
        list_products.append(el.group("product"))
        total_price +=  ((float(el.group("price")) * (float(el.group("quantity")))))
    product = input()

print("Bought furniture:")
for el in list_products:
    print(el)

print(f"Total money spend: {total_price :.2f}")
