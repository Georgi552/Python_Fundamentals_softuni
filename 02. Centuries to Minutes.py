number = int(input())

years = number * 100
days = int(years * 365.2422)
hours = int(days * 24)
min = int(hours * 60)

print(f"{number} centuries = {years} years = {days} days = {hours} hours = {min} minutes")
