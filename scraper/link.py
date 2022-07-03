import requests
from bs4 import BeautifulSoup
from scraper.headers import headers


url = 'https://www.google.com/search'

def get_link(song, source):
    final_search = song + " " + "song lyrics in:" + source
    parameters = {'q': final_search}

    content = requests.get(url, headers = headers, params = parameters).text

    content = requests.get(url, headers = headers, params = parameters).text
    soup = BeautifulSoup(content, 'html.parser')

    search = soup.find(id = 'search')
    first_link = search.find('a')

    return first_link['href']