text = input()
result = text[0]
for i in range(len(text)):
    if result[-1] == text[i]:
        pass
    else:result += text[i]
print(result)