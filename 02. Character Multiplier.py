words = input().split(" ")
result = 0
word1 = words[0]
word2 = words[1]
shorter_word = min(len(word1), len(word2))
longer_word = max(len(word1), len(word2))

str_loger_word = ""
if len(word1) > len(word2):
    str_loger_word = word1
else:
    str_loger_word = word2


for i in range(shorter_word):
    result += ord(word1[i]) * ord(word2[i])

for i in range(shorter_word, longer_word):
    result += ord(str_loger_word[i])

print(result)