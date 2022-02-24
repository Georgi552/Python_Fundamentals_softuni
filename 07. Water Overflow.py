n = int(input())

amount = 0
for m in range(0, n):
    liters = int(input())
    if amount + liters > 255:
        print("Insufficient capacity!")
    if amount + liters <= 255:
        amount += liters
print(amount)