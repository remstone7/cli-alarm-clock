# put some youtube links in json file
#     program will read the file.
# You have to set time whatever you want in any format
#     and at that particular time
#     program will pick a random link which are saved in the file
#     and start playing youtube video

import json
import random
import time
import webbrowser
song_list = []

def main():
    set_time_from_now()

with open('sound.json') as data_file:
    data = json.load(data_file)
    for s in data['songs']:
        song_list.append(s['url'])


def set_time_from_now():
    user_input = input('How long would you like until music goes off (seconds): ')
    user_input = int(user_input)
    time.sleep(user_input)

    play_song()

def play_song():
    song = random.choice(song_list)
    webbrowser.open(song)


if __name__ == '__main__':
    main()
