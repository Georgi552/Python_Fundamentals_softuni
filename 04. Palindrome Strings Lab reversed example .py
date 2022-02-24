word_list = input().split(" ")
searced_palindrome = input()

palindrome_list = []
counter = 0
for el in word_list:
    if el == "".join(reversed(el)):
        palindrome_list.append(el)
print(palindrome_list)

for el in word_list:
    if el == searced_palindrome:
        counter += 1
print(f"Found palindrome {counter} times")