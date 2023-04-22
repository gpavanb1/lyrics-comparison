import os
import openai
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Set up OpenAI API credentials
openai.api_key = os.environ.get('OPENAI_API_KEY')

def get_lyrics(song_title, song_artist):
    # Prompt to generate lyrics
    prompt = f'Get the song lyrics for {song_title} by {song_artist}'

    # Generate lyrics using OpenAI's GPT-3 API
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    lyrics = response.choices[0].text.strip()

    return lyrics