tail = input()
body = input()
head = input()

surikat = [tail, body, head]
surikat[0], surikat[2] = surikat[2], surikat[0]
print(surikat)