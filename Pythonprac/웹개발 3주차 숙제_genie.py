import requests
from bs4 import BeautifulSoup

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20220923',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')

songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# print(songs)

for song in songs:
    rank = song.select_one('tr.list > td.number').text[0:2]
    title = song.select_one('tr.list > td.info > a.title.ellipsis').text
    artist = song.select_one('tr.list > td.info > a.artist.ellipsis').text
    print(rank.strip(), title.strip(), '-', artist.strip())
