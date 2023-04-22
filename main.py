"""
usage: python main.py "pudhu vellai mazhai" "paruvam vanaga"
"""
import sys
from lyrics.genius import get_lyrics
from constants import DEFAULT_ARTIST
from utils import similarity


# Parse arguments
if len(sys.argv) < 3:
    raise Exception('Insufficient arguments specified')

# Change this
TAMIL_SONG = sys.argv[1]
TELUGU_SONG = sys.argv[2]
ARTIST = sys.argv[3] if not None else DEFAULT_ARTIST

print(f"Comparing \"{TAMIL_SONG}\" and \"{TELUGU_SONG}\"")


lyrics_a = get_lyrics(TAMIL_SONG, ARTIST)
lyrics_b = get_lyrics(TELUGU_SONG, ARTIST)
score = similarity(lyrics_a, lyrics_b)

# Summary
print('')
print('Summary')
print(lyrics_a[:25])
print(lyrics_b[:25])
print(score)