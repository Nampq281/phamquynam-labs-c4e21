import pyexcel
from youtube_dl import YoutubeDL

rank_list = pyexcel.get_records(file_name='itune_rank.xlsx')

for item in rank_list:
    title = item['Song']
    artist = item['Artist']
    search = title + "-" + artist
    
    options = {
        'default_search':'ytsearch',
        'maxdownloads':1,
        'format':'bestaudio/audio'
    }
    dl = YoutubeDL(options)

    dl.download([searh])
    print(title, 'downloaded')