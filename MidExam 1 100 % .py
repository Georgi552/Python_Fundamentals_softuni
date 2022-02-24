food = float(input())
hay = float(input())
cover = float(input())
pigs_weight = float(input())

needed_food = 0
needed_hay = 0
needed_cover = 0


for day in range(1, 31):
    food -= 0.3
    if day % 2 == 0:
        hay -= 0.05 * food
    if day % 3 == 0:
        cover -= pigs_weight / 3


if needed_hay <= hay and needed_cover <= cover and needed_food <= food:
    print(f"Everything is fine! Puppy is happy! Food: {food - needed_food :.2f}, Hay: {hay - needed_hay :.2f}, Cover: {cover - needed_cover :.2f}.")

else:
    print(f"Merry must go to the pet store!")
