import requests
from bs4 import BeautifulSoup

# Read URL for HTML
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)


# Use BeautifulSoup to parse the HTML
soup = BeautifulSoup(data.text, 'html.parser')

# Bring the list of songs from tbody
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
# Loop the song list and print results
cnt = 1
for song in songs:
    ranking = song.select_one('tr:nth-child(%i) > td.number' %cnt).text.split('\n')[0]
    #check if title is valid
    title = song.select_one('td.info > a.title.ellipsis').text.strip()
    if title is not None:
        singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
        print('%s %s %s' %(ranking, title, singer))
        cnt += 1
        if cnt > 50:
            break
    
   


