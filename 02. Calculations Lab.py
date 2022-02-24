def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

function = str(input())
num1 = int(input())
num2 = int(input())

if function == "multiply":
    print(f"{multiply(num1, num2):.0f}")

elif function == "divide":
    print(f"{divide(num1, num2):.0f}")

elif function == "add":
    print(f"{add(num1, num2):.0f}")

elif function == "subtract":
    print(f"{subtract(num1, num2):.0f}")
