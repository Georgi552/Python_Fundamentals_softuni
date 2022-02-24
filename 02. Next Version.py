current_version = input().split(".")
new_version = [0, 0, 0]
new_version[0], new_version[1], new_version[2] = int(current_version[0]), int(current_version[1]), (int(current_version[2]) + 1)
if new_version[2] > 9:
    new_version[2] = 0
    new_version[1] = new_version[1] + 1
    if new_version[1] > 9:
        new_version[1] = 0
        new_version[0] = new_version[0] + 1

new_version_str = []
for el in new_version:
    new_version_str.append(str(el))

new_str = ''.join(new_version_str)

print(f"{'.'.join(new_str)}")