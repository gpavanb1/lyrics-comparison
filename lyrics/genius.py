import os
from dotenv import load_dotenv
import lyricsgenius

# Access the constant value
GENIUS_API_KEY = int(os.environ.get('GENIUS_API_KEY'))

# Load the .env file
load_dotenv()

# Replace YOUR_API_KEY with your own Genius API key
genius = lyricsgenius.Genius(GENIUS_API_KEY)

def get_lyrics(song_title, song_artist):
    # Search for the lyrics of a song
    song = genius.search_song(song_title, song_artist)

    # Print the lyrics if the song is found
    if song is not None:
        print(song.lyrics)
    else:
        raise Exception("Sorry, the lyrics could not be found")