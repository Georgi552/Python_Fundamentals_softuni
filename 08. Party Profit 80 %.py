party_size = int(input())
days = int(input())

earnings = 0
spend = 0
counter = 0
for day in range(0, days):
    earnings += 50
    spend += (2 * party_size)
    counter += 1
    if counter % 15 == 0:
        party_size += 5
    if counter % 10 == 0:
        party_size -= 2
    if counter % 3 == 0:
        spend += (3 * party_size)
    if counter % 5 == 0:
        earnings += (20 * party_size)
        if counter % 3 == 0:
            spend += (2 * party_size)
import math

profit = math.floor(earnings - spend)

print(f"{party_size} companions received {math.floor(profit / party_size)} coins each.")

