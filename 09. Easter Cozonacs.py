budget = float(input())
flour_price = float(input())

egs = flour_price * 0.75
milk = (flour_price * 1.25) / 4
cozunak_price = flour_price + egs + milk
total_egs = 0
counter = 0
while cozunak_price < budget:
    budget -= cozunak_price
    total_egs += 3
    counter += 1
    if counter % 3 == 0:
        reduction = counter - 2
        if reduction < 0:
            reduction = 0
        total_egs -= reduction

print(f"You made {counter} cozonacs! Now you have {total_egs} eggs and {budget :.2f}BGN left.")