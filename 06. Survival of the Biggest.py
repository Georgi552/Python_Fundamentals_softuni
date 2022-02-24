List = input().split(" ")
n = int(input())

for i in range(len(List)):
    List[i] = int(List[i])

for o in range(n):
    min_element = min(List)
    List.remove(min_element)

for t in range(len(List)):
    List[t] = str(List[t])


print(", ".join(List))