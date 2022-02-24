text = str(input())

text_list = [text]

int_list = [int(s) for s in text.split(' ')]
reverse_list = []
for i in range(len(int_list)):
    element = int_list[i]

    reverse_list.append(-element)

print(reverse_list)