n = int(input())
total = 0
for number in range(1, n + 1):
    code = input()
    total += ord(code)

print(f"The sum equals: {total}")
