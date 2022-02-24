username = input()

pre_comand = input()
while not pre_comand == "Sign up":
    comand = pre_comand.split(" ")
    if comand[0] == "Case":
        if comand[1] == "lower":
            username = username.lower()
            print(username)
        if comand[1] == "upper":
            username = username.upper()
            print(username)
    if comand[0] == "Reverse":
        if int(comand[2]) >= len(username):
            pass
        else:
            result = username[int(comand[1]) : int(comand[2]) + 1]
            rev_result = result[::-1]
            print(rev_result)
    if comand[0] == "Cut":
        if comand[1] in username:
            username = username.replace(comand[1], "")
            print(username)
        elif comand[1] not in username:
            print(f"The word {username} doesn't contain {comand[1]}.")
    if comand[0] == "Replace":
        result = username
        while comand[1] in username:
            username = username.replace(comand[1], "*")
            print(username)
    if comand[0] == "Check":
        if comand[1] in username:
            print(f"Valid")
        elif comand[1] not in username:
            print(f"Your username must contain {comand[1]}.")

    pre_comand = input()