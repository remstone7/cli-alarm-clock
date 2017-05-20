# put some youtube links in text file
#     program will read the file.
# You have to set time whatever you want in any format
#     and at that particular time
#     program will pick a random link which are saved in the file
#     and start playing youtube video

import json

song_list = []

with open('sound.json') as data_file:
    data = json.load(data_file)
    for s in data['songs']:
        song_list.append(s['url'])
