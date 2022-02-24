def price_total(product, quantity):
    if product == "coffee":
        return quantity * 1.5
    if product == "water":
        return quantity * 1.0
    if product == "coke":
        return quantity * 1.4
    if product == "snacks":
        return quantity * 2.0

stock = input()
number = int(input())

print(f"{price_total(stock, number) :.2f}")