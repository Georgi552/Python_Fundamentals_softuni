dict = {}
words = input().split(" ")
for word in words:
    word_lower = word.lower()
    if word_lower not in dict:
        dict[word_lower] = 0
    else:
        dict[word_lower] += 1
for x, y in dict.items():
    if y % 2 == 0:
        print(x, end=" ")