def get_lyrics(song_title, lang):
    # Convert song title to filename
    fname = song_title.lower().replace(' ', '_')

    # Open file
    if lang == 'te':
        fname = f'./lyrics_text/telugu/{fname}.txt'
    elif lang == 'ta':
        fname = f'./lyrics_text/tamil/{fname}.txt'
    else:
        raise Exception('Incorrect language specified')
    
    with open(fname, "r") as f:
        contents = f.read()

    return contents

    
