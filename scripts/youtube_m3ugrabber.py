#! /usr/bin/python3

banner = r'''
#########################################################################
#      ____            _           _   __  __                           #
#     |  _ \ _ __ ___ (_) ___  ___| |_|  \/  | ___   ___  ___  ___      #
#     | |_) | '__/ _ \| |/ _ \/ __| __| |\/| |/ _ \ / _ \/ __|/ _ \     #
#     |  __/| | | (_) | |  __/ (__| |_| |  | | (_) | (_) \__ \  __/     #
#     |_|   |_|  \___// |\___|\___|\__|_|  |_|\___/ \___/|___/\___|     #
#                   |__/                                                #
#                                  >> https://github.com/benmoose39     #
#########################################################################
'''

import requests
import os
import sys

windows = False
if 'win' in sys.platform:
    windows = True

def grab(url):
    response = requests.get(url, timeout=15).text
    if '.m3u8' not in response:
        #response = requests.get(url).text
        if '.m3u8' not in response:
            if windows:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
            #os.system(f'wget {url} -O temp.txt')
            os.system(f'curl "{url}" > temp.txt')
            response = ''.join(open('temp.txt').readlines())
            if '.m3u8' not in response:
                print('https://raw.githubusercontent.com/benmoose39/YouTube_to_m3u/main/assets/moose_na.m3u')
                return
    end = response.find('.m3u8') + 5
    tuner = 100
    while True:
        if 'https://' in response[end-tuner : end]:
            link = response[end-tuner : end]
            start = link.find('https://')
            end = link.find('.m3u8') + 5
            break
        else:
            tuner += 5
    print(f"{link[start : end]}")

print(banner)
#s = requests.Session()
with open('../youtube_channel_info.txt') as f:
    for line in f:
        line = line.strip()
        if not line or line.startswith('~~'):
            continue
        if not line.startswith('https:'):
            line = line.split('|')
            ch_name = line[0].strip()
            grp_title = line[1].strip().title()
            tvg_logo = line[2].strip()
            tvg_id = line[3].strip()
            print(f'\n#EXTINF:-1 group-title="{grp_title}" tvg-logo="{tvg_logo}" tvg-id="{tvg_id}", {ch_name}')
        else:
            grab(line)
print(f'\n#EXTINF:-1 group-title="Rock" tvg-logo="https://upload.wikimedia.org/wikipedia/commons/thumb/8/89/Logo-b6f7b5.jpg/800px-Logo-b6f7b5.jpg" tvg-id="", Radio Maximum\nhttps://hls-01-maximum.hostingradio.ru/maximum/112/playlist.m3u8')
print(f'\n#EXTINF:-1 group-title="Rock" tvg-logo="https://radioultra.ru/storage/87229/conversions/cover-social.jpg" tvg-id="", Radio Ultra\nhttps://nashe1.hostingradio.ru/ultra-128.mp3')
print(f'\n#EXTINF:-1 group-title="Sovietwave" tvg-logo="https://cdnb.artstation.com/p/assets/images/images/031/727/841/large/danylo-hrechyshkin-untitled-4.jpg" tvg-id="", Radio Sovietwave\nhttp://station.waveradio.org/soviet.mp3')
if 'temp.txt' in os.listdir():
    os.system('rm temp.txt')
    os.system('rm watch*')
