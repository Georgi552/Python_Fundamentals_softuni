deck = input().split("\n")
n_shufles = int(input())
left_half = []
right_half = []

for shuffle in range(n_shufles):
    current_deck = []
    half = int(len(deck)/2)
    left_half = deck[0: half]
    right_half = deck[half::]
    for card in range(len(left_half)):
        current_deck.append(left_half[card])
        current_deck.append(right_half[card])
    deck = current_deck
print(deck)
