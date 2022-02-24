factor = int(input())
count = int(input())
list_1 = []
import sys
while len(list_1) < count:
    for number in range(1, sys.maxsize):
        if number % factor == 0:
            list_1.append(number)
        if len(list_1) >= count:
            break
print(list_1)