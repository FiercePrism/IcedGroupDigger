import requests , random , threading , ctypes
print('''
This was coded by Andrade#0829 
Only change webhooks! 
If you skid this, there WILL be conequnces applied.
''')
thread_count = int(input('How many threads do you want? : '))

url = "    "    # Webhooks Here.
url2 = "     "  # Webhooks Here.
imu = ""


def sendmessage(webURL, groupID, name, memberCount, robux, description, imu, date):
    data = {
        "username": "IcedBruteForcer",
        "avatar_url": "",
        "embeds": [
        {
            "author": {
            "name": "IcedBruteForcer",
            "url": "",
            "icon_url": ""
        },
            "title": "Group Name: " + str(name),
            "color": random.randint(100000,500000),
            "fields": [
                 {
                "name": "Total Member",
                "value": str(memberCount) + " Members",
                "inline": True
            },
                 {
                "name": "Total R$",
                "value": str(robux),
                "inline": True
            },
            {
                "name": "Group Link",
                "value": 'https://www.roblox.com/groups/' + str(groupID),
                "inline": True
            },
            {
                "name": "Group Description",
                "value": str(description),
                "inline": True
            },
        ],
            "image": {
                "url": imu
            },
            "footer": {
             "text": "Made by Andrade#0829" + str(date),
                         "icon_url": ""
            }
        }
	    ]
    }
    h = requests.post(webURL, json=data)

groups_valid = 0
groups_scanned = 0
robux = 0
groups_list = []
groups_removed = 0
def group_scanning():
    while True:
        try:
            global groups_valid
            global groups_scanned
            global robux
            global groups
            global groups_removed

            ctypes.windll.kernel32.SetConsoleTitleW('GroupDigger | TotalChecking : {}  | GroupsValid : {} | R$Earned : {} | by Andrade'.format(groups_scanned,groups_valid,groups_removed,robux))
            groupID = random.randint(1,5901231)

            checking = requests.get('https://groups.roblox.com/v1/groups/{}'.format(groupID))
            currency = requests.get('https://economy.roblox.com/v1/groups/{}/currency'.format(groupID))

            groups_scanned += 1

            if checking.status_code != 200:
                continue
            else:
                if 'isLocked' in checking.json():
                    continue
                else:
                    if checking.json()['publicEntryAllowed'] == False or checking.json()['owner'] != None:
                        continue
                    else:

                        
                        if groupID not in groups_list:
                            groups_list.append(groupID)
                            groups_valid += 1
                        else:
                            groups_removed += 1
                            continue

                        if currency.status_code == 200 and currency.json()['robux'] > 0:
                            print('>> {} | Robux : {} | {}\n'.format(checking.json()['id'],currency.json()['robux'], currency.json()))
                            robux += currency.json()['robux']
                            with open('groups_robux.txt','a',encoding='UTF-8') as f:
                                f.write('{} | {} | {} | Robux : {}\n'.format(checking.json()['id'],checking.json()['name'],'https://www.roblox.com/groups/' + str(groupID) + 'a',currency.json()['robux']))
                            sendmessage(url, checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], currency.json()['robux'], checking.json()['description'], imu, "26/05/2019")
                        else:
                            sendmessage(url2, checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], 0, checking.json()['description'], imu, "26/05/2019")
                            print('>> {} | No Owner | {}\n'.format(checking.json()['id'], checking.json()['name'], checking.json()['memberCount'], currency.json()))
                            with open('groups.txt','a',encoding='UTF-8') as f:
                                f.write('{} | {} | {} \n'.format(checking.json()['id'],checking.json()['name'] ,'https://www.roblox.com/groups/' + str(groupID) + '/a'))
        except Exception as e:
            print(e)


for x in range(thread_count):
    threading.Thread(target=group_scanning).start()
