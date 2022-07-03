"""
usage: python main.py "pudhu vellai mazhai" "paruvam vanaga"
"""
import sys
from scraper.gaana import get_lyrics
from utils import similarity


# Parse arguments
if len(sys.argv) < 3:
    raise Exception('Insufficient arguments specified')

# Change this
TAMIL_SONG = sys.argv[1]
TELUGU_SONG = sys.argv[2]

print(f"Comparing \"{TAMIL_SONG}\" and \"{TELUGU_SONG}\"")


lyrics_a = get_lyrics(TAMIL_SONG)
lyrics_b = get_lyrics(TELUGU_SONG)
score = similarity(lyrics_a, lyrics_b)

# Summary
print('')
print('Summary')
print(lyrics_a[:25])
print(lyrics_b[:25])
print(score)