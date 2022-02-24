divisor = int(input())
bound = int(input())
import sys
number1 = -sys.maxsize
for number in range(1,bound +1):
    if number % divisor == 0:
        if number > number1:
            number1 = number

print(number1)