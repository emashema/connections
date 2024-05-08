import requests
import datetime
import os, os.path
from json import dumps

############################################################################
# Script to scrape the NY Times connections puzzles from the past 365 days #
# in order to use them as data (different puzzle every day) :)             #
############################################################################

today = datetime.date.today()
date_list = [today - datetime.timedelta(days=x) for x in range(1500)]
i=0
d=0

while len([f for f in os.listdir('./connections/')]) != 365:
    i+=1

    response = requests.get(f'https://www.nytimes.com/svc/connections/v2/{str(date_list[d])}.json')
    data = response.json()

    if data['status'] == 'OK':
        obj = []
        level = 1
        for category in data['categories']:
            obj.append({
                "level": level,
                "key": category['title'],
                "values": list(map(lambda x: x['content'], category['cards']))
            })
            level += 1

        json_obj = dumps(obj, indent=4)

        with open(f'./connections/{i}.json', "w") as file:
            file.write(json_obj)

    d+=1