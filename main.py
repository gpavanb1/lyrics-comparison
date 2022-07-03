from scraper.gaana import get_lyrics
from scraper.link import get_link
from utils import similarity


SOURCE_SONG = "pudhu vellai mazhai"
SOURCE_LANG = "Tamil"

DEST_LANG = "Telugu"
# DEST_SONG = get_song(SOURCE_SONG, DEST_LANG)


lyrics_a = get_lyrics(SOURCE_SONG)
lyrics_b = get_lyrics(DEST_SONG)
score = similarity(lyrics_a, lyrics_b, SOURCE_LANG, DEST_LANG)
print(score)