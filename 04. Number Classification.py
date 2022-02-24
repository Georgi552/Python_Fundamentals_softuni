text = input().split(", ")
positive = [(el) for el in text if int(el) >= 0]
negative = [(el) for el in text if int(el) < 0]
evan = [(el) for el in text if int(el) % 2 == 0]
odd = [(el) for el in text if not int(el) % 2 == 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(evan)}")
print(f"Odd: {', '.join(odd)}")