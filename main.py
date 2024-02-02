"""
usage: python main.py "pudhu vellai mazhai" "paruvam vanaga"
"""
import argparse
from lyrics.local import get_lyrics as get_local
from constants import DEFAULT_ARTIST
from utils import similarity, get_lyrics_source


parser = argparse.ArgumentParser()
parser.add_argument("--mode", choices=["local", "global"], default="local")
parser.add_argument(
    "--source", choices=["genius", "openai"], default="genius", required=False)
args = parser.parse_args()

ARTIST = DEFAULT_ARTIST

if args.mode == "local":
    print("Running in local mode")
elif args.mode == "global":
    print("Running in global mode")
else:
    raise Exception('Incorrect mode specified')

TAMIL_SONG = input('Enter name of Tamil song: ')
TELUGU_SONG = input('Enter name of Telugu song: ')

print(f"Comparing \"{TAMIL_SONG}\" and \"{TELUGU_SONG}\"")

if args.mode == 'local':
    lyrics_a = get_local(TAMIL_SONG, lang='ta')
    lyrics_b = get_local(TELUGU_SONG, lang='te')
elif args.mode == 'global':
    lyrics_a = get_lyrics_source(TAMIL_SONG, ARTIST, args.source)
    lyrics_b = get_lyrics_source(TELUGU_SONG, ARTIST, args.source)
score = similarity(lyrics_a, lyrics_b)

# Summary
print('')
print('Summary')
print(lyrics_a[:25] + '...')
print(lyrics_b[:25] + '...')
print('')
print(f"Similarity: {round(score, 2)}")
