list = input().split(", ")

dict = {el: ord(el) for el in list}

#for el in list:
   # dict[el] = ord(el)
print(dict)