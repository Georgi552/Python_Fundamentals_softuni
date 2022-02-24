n = int(input())
numbers_list = []
filtered_list = []

for c in range(n):
    number = int(input())
    numbers_list.append(number)
comand = str(input())
if comand == "even":
    for n in range(len(numbers_list)):
        element = numbers_list[n]
        if element % 2 == 0:
            filtered_list.append(element)

if comand == "odd":
    for n in range(len(numbers_list)):
        element = numbers_list[n]
        if not element % 2 == 0:
            filtered_list.append(element)


if comand == "positive":
    for n in range(len(numbers_list)):
        element = numbers_list[n]
        if element >= 0:
            filtered_list.append(element)

if comand == "negative":
    for n in range(len(numbers_list)):
        element = numbers_list[n]
        if element < 0:
            filtered_list.append(element)

print(filtered_list)
