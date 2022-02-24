import re

product = input()
dict_products = {}
while not product == "Purchase":
    pattern = r">>(?P<product>[a-zA-Z]*)<<(?P<price>\d+[\.\d+]*)!(?P<quantity>\d+)"
    matches = re.finditer(pattern, product)
    for el in matches:
        dict_products[el.group("product")] =  ((float(el.group("price")) * (float(el.group("quantity")))))
    product = input()
total_price = 0
print("Bought furniture:")
for k, v in dict_products.items():
    print(k)
    total_price += v
print(f"Total money spend: {total_price :.2f}")
