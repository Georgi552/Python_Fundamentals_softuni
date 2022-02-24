hapines = input().split(" ")
factor = int(input())

new_happynes = [int(el) * factor for el in hapines]
above_average_happy = [el for el in new_happynes if el >= (sum(new_happynes) / len(new_happynes))]

if len(above_average_happy) >= (len(new_happynes) / 2):
    print(f"Score: {len(above_average_happy)}/{len(new_happynes)}. Employees are happy!")

if len(above_average_happy) < (len(new_happynes) / 2):
    print(f"Score: {len(above_average_happy)}/{len(new_happynes)}. Employees are not happy!")