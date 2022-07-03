import requests
from bs4 import BeautifulSoup

from scraper.link import get_link
from scraper.headers import headers


def get_lyrics(song):
    link = get_link(song, "gaana.com")
    content = requests.get(link, headers = headers).text
    soup = BeautifulSoup(content, 'html.parser')
    lyrics_data = soup.find_all('div', {"class": "_inner"})
    lyrics_ps = lyrics_data[1].findAll('p')
    lyrics = []
    for lyrics_p in lyrics_ps:
        lyrics.append(lyrics_p.text.replace('\n', ' '))
    lyrics = ' '.join(lyrics)
    return lyrics
