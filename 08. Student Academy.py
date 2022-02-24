n = input()
counter = 0

dic_students = {}

while counter < int(n):
    counter += 1
    name = input()
    grade = float(input())
    if name not in dic_students:
        dic_students[name] = []
        dic_students[name] = [grade]
    elif name in dic_students:
        dic_students[name].append(grade)

dic_students_average = {}
ocenka = 0
delitel = 1
for k, v in dic_students.items():
    for el in v:
        ocenka += el
        delitel += 1
    dic_students_average[k] = ocenka / (delitel - 1)
    ocenka = 0
    delitel = 1


dic_students_average_sored = dict(sorted(dic_students_average.items() , key=lambda x : x[1], reverse=True))
dic_students_average_sored_above_450 = {}
for k, v in dic_students_average_sored.items():
    if v >= 4.50:
        dic_students_average_sored_above_450[k] = v
for k, v in dic_students_average_sored_above_450.items():
    print(f"{k} -> {float(v) :.2f}")