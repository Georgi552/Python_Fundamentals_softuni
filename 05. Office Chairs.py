n = int(input())
free_chairs = 0
counter = 0
for el in range(n):
    chairs = input().split(" ")
    if len(chairs[0]) >= int(chairs[1]):
        free_chairs += (len(chairs[0]) - int(chairs[1]))
    if len(chairs[0]) < int(chairs[1]):
        counter += 1
        print(f"{int(chairs[1]) - len(chairs[0])} more chairs needed in room {el + 1}")
if counter == 0:
     print(f"Game On, {free_chairs} free chairs left")
