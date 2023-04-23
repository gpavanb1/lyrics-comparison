# Lyrics Comparison

![Made with Love in India](https://madewithlove.org.in/badge.svg)

Compare lyrics between languages by just providing the title

This repository contains integration to [Genius API client](https://docs.genius.com/) or [OpenAI](https://openai.com/blog/openai-api) for fetching lyrics and uses [Spacy](https://spacy.io/) and [indic_transliteration](https://pypi.org/project/indic-transliteration/) for translating and calculating similarity.

## How to execute?

Just run 
```
python main.py --mode [global, local] <--source [genius, openai]> 
```

Those in `[` indicate possible options and those in `<` indicate optional arguments

## Local lyrics translation

To utilize lyrics that are available locally, please create a `lyrics_text` folder with subfolders as `tamil` and `telugu`

You can then add files with song names in lowercase and spaces replaced by `_`. For example, in `lyrics_text/tamil`, you can have a file named `pachai_nirame.txt`.

We will leave it upto the user to source lyrics from an appropriate source.
## Whom to contact?

Please direct your queries to [gpavanb1](http://github.com/gpavanb1)
for any questions.
