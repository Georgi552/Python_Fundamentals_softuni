dict_social_media = {}
action = input()
while not action == "Log out":
    list_action = action.split(": ")
    if list_action[0] == "New follower":
        if list_action[1] not in dict_social_media:
            dict_social_media[list_action[1]] = {}
            dict_social_media[list_action[1]]['likes'] = 0
            dict_social_media[list_action[1]]['comments'] = 0
            dict_social_media[list_action[1]]['total'] = 0

        elif list_action[1] in dict_social_media:
            pass
    if list_action[0] == "Like":
        if list_action[1] not in dict_social_media:
            dict_social_media[list_action[1]] = {}
            dict_social_media[list_action[1]]['likes'] = int(list_action[2])
            dict_social_media[list_action[1]]['comments'] = 0
            dict_social_media[list_action[1]]['total'] = int(list_action[2])
        elif list_action[1] in dict_social_media:
            dict_social_media[list_action[1]]['likes'] += int(list_action[2])
            dict_social_media[list_action[1]]['total'] += int(list_action[2])
    if list_action[0] == "Comment":
        if list_action[1] not in dict_social_media:
            dict_social_media[list_action[1]] = {}
            dict_social_media[list_action[1]]['likes'] = 0
            dict_social_media[list_action[1]]['comments'] = 1
            dict_social_media[list_action[1]]['total'] = 1
        elif list_action[1] in dict_social_media:
            dict_social_media[list_action[1]]['comments'] += 1
            dict_social_media[list_action[1]]['total'] += 1
    if list_action[0] == "Blocked":
        if list_action[1] not in dict_social_media:
            print(f"{list_action[1]} doesn't exist.")
        elif list_action[1] in dict_social_media:
            del dict_social_media[list_action[1]]




    action = input()

print(f"{len(dict_social_media)} followers")
new_dict = {}
for k, v in dict_social_media.items():
    for x, y in v.items():
        if x == "total":
            new_dict[k] = y

sorted_list = sorted(new_dict.items(), key=lambda x: -x[1])
dict_social_media_sorted = dict(sorted_list)


for k, v in dict_social_media_sorted.items():

        print(f"{k}: {v}")
