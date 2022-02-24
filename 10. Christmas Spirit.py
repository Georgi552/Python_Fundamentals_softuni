qauantity = int(input())
days = int(input())
chrismans_spirit = 0
counter = 0
ornament_sets = 0
three_skirts = 0
three_grliands = 0
three_lights = 0

while days > 0:
    days -= 1
    counter += 1
    if counter % 11 == 0:
        qauantity += 2

    if counter % 2 == 0:
        ornament_sets += qauantity
        chrismans_spirit += 5
    if counter % 3 == 0:
        three_grliands += qauantity
        three_skirts += qauantity
        chrismans_spirit += 13
    if counter % 5 == 0:
        three_lights += qauantity
        chrismans_spirit += 17
        if counter % 3 == 0:
            chrismans_spirit += 30
    if counter % 10 == 0:
        chrismans_spirit -= 20
        three_skirts += 1
        three_lights += 1
        three_grliands += 1

if counter % 10 == 0:
    chrismans_spirit -= 30
budget = (ornament_sets * 2) + (three_skirts * 5) + (three_grliands * 3) + (three_lights * 15)
print(f"Total cost: {budget}")
print(f"Total spirit: {chrismans_spirit}")




