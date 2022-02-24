resourse = input()


dict_res = {}
while not resourse == "stop":
    quantity = input()
    if resourse not in dict_res:
        dict_res[resourse] = int(quantity)

    elif resourse in dict_res:
        dict_res[resourse] += int(quantity)


    resourse = input()

if resourse == "stop":
    for key, value in dict_res.items():
        print(f"{key} -> {value}")