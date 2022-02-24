comand = input()

dic_company_emplyees = {}
while not comand == "End":
    list_comand = comand.split(" -> ")
    company_name = list_comand[0]
    emplyee_id = list_comand[1]
    if company_name not in dic_company_emplyees:
        if emplyee_id not in dic_company_emplyees:
            dic_company_emplyees[company_name] = []
            dic_company_emplyees[company_name] = [emplyee_id]
        elif emplyee_id in dic_company_emplyees:
            pass
    elif company_name in dic_company_emplyees:
        for k, v in dic_company_emplyees.items():
            if company_name == k:
                if emplyee_id in v:
                    break
                for el in v:
                    if el not in emplyee_id:
                        dic_company_emplyees[company_name].append(emplyee_id)
                        break





    comand = input()

sorted_dic_company_emplyees = dict(sorted(dic_company_emplyees.items(), key=lambda  x: x[0]))
for k, v in sorted_dic_company_emplyees.items():
    print(f"{k}")
    for el in v:
        print(f"-- {el}")


