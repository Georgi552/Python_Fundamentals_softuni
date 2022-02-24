A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11]
B = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10 , 11]

sequence = str(input())
list = sequence.split(" ")

deductin = 0
deductin_list = []
deducted_player = 0

for simbols in list:
    deductin = simbols
    deductin_list = deductin.split("-")
    if deductin_list[0] == "A":
        for player in A:
            deducted_player = int(deductin_list[1])
            if player == deducted_player:
                A.remove(player)
            else:
                pass
                if len(A) < 7:
                    break

    if deductin_list[0] == "B":
        for player in B:
            deducted_player = int(deductin_list[1])
            if player == deducted_player:
                B.remove(player)
                if len(B) < 7:
                    break
            else:
                pass
    else:
        pass

print(f"Team A - {len(A)}; Team B - {len(B)}")

if len(A) < 7 or len(B) < 7:
    print("Game was terminated")