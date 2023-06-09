import os
import lyricsgenius
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Access the constant value
GENIUS_ACCESS_TOKEN = os.environ.get('GENIUS_ACCESS_TOKEN')

genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)

def get_lyrics(song_title, song_artist):
    # Search for the lyrics of a song
    song = genius.search_song(song_title, song_artist)

    # Print the lyrics if the song is found
    if song is not None:
        return song.lyrics
    else:
        raise Exception("Sorry, the lyrics could not be found")