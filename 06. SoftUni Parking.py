n = input()


registered = {}
counter = 0
while  counter < int(n):

    comand = input().split(" ")

    if comand[0] == "register":
        action = comand[0]
        username = comand[1]
        registration_plate = comand[2]
        if username not in registered:
            registered[username] = registration_plate
            print(f"{username} registered {registration_plate} successfully")
        else:
            for key, value in registered.items():
                if key == username:
                    print(f"ERROR: already registered with plate number {value}")

    if comand[0] == "unregister":
        action = comand[0]
        username = comand[1]

        if username in registered.keys():
            print(f"{username} unregistered successfully")
            registered.pop(username)
        else:
            print(f"ERROR: user {username} not found")
    counter += 1
if counter == int(n):
    for key, value in registered.items():
        print(f"{key} => {value}")