from youtube_dl import YoutubeDL
from urllib.request import urlopen
from bs4 import BeautifulSoup
import pyexcel

url = "https://www.apple.com/itunes/charts/songs/"
conn = urlopen(url)
raw_data = conn.read()

html_page = raw_data.decode('utf-8')
f_conn = open('itunecharts.html','wb')
f_conn.write = raw_data
f_conn.close()
soup = BeautifulSoup(html_page,"html.parser")

section = soup.find('section','section chart-grid')
li_list = section.find_all('li')

rank_list =[]
for li in li_list:
    rank = li.strong.string
    song = li.h3.a.string
    artist = li.h4.a.string
    ranking = {
        "Rank": rank,
        "Song": song,
        "Artist": artist,
    }
    rank_list.append(ranking)
print(rank_list)
pyexcel.save_as(records = rank_list, dest_file_name = 'itune_rank.xlsx' )
print('done')