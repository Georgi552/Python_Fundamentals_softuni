n = int(input())
counter = 0
shels = []
while n > 0:
    counter += 1
    if (n - (2 * counter ** 2)) >= 0:
        n -= (2 * counter ** 2)
        shels.append((2 * counter ** 2))
    else:
        shels.append(n)
        n = 0
print(shels)



