dict_students = {}
student = input()

while not student.islower():
    list_student = student.split(':')
    if list_student[2] not in dict_students:
        dict_students[list_student[2]] = {}
    dict_students[list_student[2]][list_student[1]] = list_student[0]


    student = input()
course = " ".join(student.split("_"))
for key, value in dict_students.items():
    if key == course:
        for id, name in value.items():
            print(f"{name} - {id}")

