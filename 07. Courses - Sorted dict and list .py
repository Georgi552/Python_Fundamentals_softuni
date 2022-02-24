comand = input()
dic_courses = {}

while not comand == "end":
    counter = 0
    comand_list = comand.split(" : ")
    course = comand_list[0]
    name = comand_list[1]
    if course not in dic_courses:
        dic_courses[course] = [name]
        counter += 1

    elif course in dic_courses:
        dic_courses[course].append(name)
        counter += 1


    comand = input()

if comand == "end":


    dic_sorted = dict(sorted(dic_courses.items(), key=lambda x: len(x[1]), reverse=True ))

    #print(dic_sorted)
    # using sorted() + join() + lambda
    # Sort dictionary by value list length
    #res = ' '.join(sorted(test_dict, key=lambda key: len(test_dict[key])))
    #print(' '.join(sorted(d, key=lambda k: len(d[k]), reverse=True)))
    #  sorted(db, key = lambda k: (-len(db[k]), k))


    for k, v, in dic_sorted.items():
        print(f"{k}: {len(v)}")
        v_sorted = sorted(v)
        for el in v_sorted:
            print(f"-- {el}")