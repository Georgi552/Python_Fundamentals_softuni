n = int(input())

synonims_dict = {}

for i in range(n):
    word = input()
    sinonim = input()
    if word not in synonims_dict:
        synonims_dict[word] = []

    synonims_dict[word].append(sinonim)

for word in synonims_dict:
    print(f"{word} - {', '.join(synonims_dict[word])}")
