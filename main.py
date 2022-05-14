import requests

channels = []
with open('channels.txt') as f:
    lines = f.readlines()
    channels = [line.rstrip() for line in lines]

for channel in channels:
    contents = requests.get('https://www.twitch.tv/' +channel).content.decode('utf-8')

    if 'isLiveBroadcast' in contents: 
        print(channel + ' is live')
    else:
        print(channel + ' is not live')