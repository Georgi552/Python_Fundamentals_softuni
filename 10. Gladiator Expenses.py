lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())

expenses = 0
counter = 0
shield_counter = 0
for lost in range(0, lost_fights):
    counter += 1
    if counter % 2 == 0:
        expenses += helmet_price
    if counter % 3 == 0:
        expenses += sword_price
        if counter % 2 == 0:
            expenses += shield_price
            shield_counter += 1
            if shield_counter % 2 == 0:
                expenses += armour_price

print(f"Gladiator expenses: {expenses:.2f} aureus")



