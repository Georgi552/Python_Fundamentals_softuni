n = int(input())
possitive_list = []
negative_list = []

for c in range(n):
    number = int(input())
    if number >= 0:
        possitive_list.append(number)
    if number < 0:
        negative_list.append(number)
print(possitive_list)
print(negative_list)
print(f"Count of positives: {len(possitive_list)}. Sum of negatives: {sum(negative_list)}")

