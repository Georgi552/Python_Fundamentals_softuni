text = input()
position = 0
result = ''

for i in range(len(text)):
    if text[i] == ":":
        result += text[i]
        result += text[i+1]
        print(result)
        result = ''