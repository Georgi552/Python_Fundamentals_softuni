deck = str(input())
n_shuffles = int(input())

deck_list = deck.split(" ")
half = len(deck_list) / 2

left_deck = []
right_deck = []

new_deck = []


for i in range(n_shuffles):
    new_deck = []
    for o in range(0, int(half)):
        left_deck.append(deck_list[o])
    for m in range(int(half), len(deck_list)):
        right_deck.append(deck_list[m])
    for k in range(int(half)):
        new_deck.append(left_deck[k])
        new_deck.append(right_deck[k])
    deck_list = new_deck
    left_deck = []
    right_deck = []

print(new_deck)

