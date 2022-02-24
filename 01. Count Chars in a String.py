text = input().split(" ")
dict = {}
for word in text:
    for el in word:
        if el not in dict:
            dict[el] = 1
        elif el in dict:
            dict[el] += 1
for key, value in dict.items():
    print(f"{key} -> {value}")