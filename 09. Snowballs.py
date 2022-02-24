n_snowbals = int(input())

snow1 = 0
time1 = 0
quality1 = 0
snowball_value = 0

for ball in range(0, n_snowbals):
    snow = int(input())
    time = int(input())
    quality = int(input())

    snowball_value_current = (snow / time) ** quality
    if snowball_value_current > snowball_value:
        snowball_value = snowball_value_current
        snow1 = snow
        time1 = time
        quality1 = quality


print(f"{snow1} : {time1} = {int(snowball_value)} ({quality1})")