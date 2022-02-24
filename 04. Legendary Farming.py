

dic_materials = {"shards":0, "motes": 0, "fragments": 0 }
dic_junk = {}
obtained = ""


while obtained == "":
    materials = input().lower().split(" ")
    for i in range(1, len(materials), 2):
        if not obtained == "":
            break
        if materials[i] == "shards":
            dic_materials["shards"] += int(materials[i - 1])
        elif materials[i] == "fragments":
            dic_materials["fragments"] += int(materials[i - 1])
        elif materials[i] == "motes":
            dic_materials["motes"] += int(materials[i - 1])
        else:
            if materials[i] not in dic_junk:
                dic_junk[materials[i]] = int(materials[i - 1])
            elif materials[i] in dic_junk:
                dic_junk[materials[i]] += int(materials[i - 1])
        for key, value in dic_materials.items():
            if value >= 250:
                if key == "shards":
                    obtained = "Shadowmourne"
                    dic_materials["shards"] -= 250


                elif key == "motes":
                    obtained = "Dragonwrath"
                    dic_materials["motes"] -= 250


                elif key == "fragments":
                    obtained = "Valanyr"
                    dic_materials["fragments"] -= 250
                break


print(f"{obtained} obtained!")

dict_materials_sorted = dict(sorted(dic_materials.items(), key=lambda  x: (-x[1], x[0])))

for key, value in dict_materials_sorted.items():

    print(f"{key}: {value}")

dic_junk_sorted = dict(sorted(dic_junk.items(), key=lambda x: x[0]))
for key, value in dic_junk_sorted.items():
    print(f"{key}: {value}")