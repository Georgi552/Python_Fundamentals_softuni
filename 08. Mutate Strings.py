firs = str(input())
second = str(input())
last = firs
for symbol in range(0, len(firs)):
     left_part = second[: symbol + 1]
     right_part = firs[symbol + 1:]
     new = left_part + right_part
     if new == last:
         continue
     print(new)
     last = new
