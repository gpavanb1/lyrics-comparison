# Lyrics Comparison

![Made with Love in India](https://madewithlove.org.in/badge.svg)

Compare lyrics between languages by just providing the title

This repository contains integration to [Genius API client](https://docs.genius.com/) or [OpenAI](https://openai.com/blog/openai-api) for fetching lyrics and uses [LaBSE](https://huggingface.co/sentence-transformers/LaBSE)[1] and [AI4Bharat transliteration](https://pypi.org/project/ai4bharat-transliteration/)[2] for translating and calculating similarity.

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

## References

[1] Feng, F., Yang, Y., Cer, D., Arivazhagan, N., & Wang, W. (2020). Language-agnostic BERT sentence embedding. arXiv preprint arXiv:2007.01852.

[2] Madhani, Y., Parthan, S., Bedekar, P., Khapra, R., Seshadri, V., Kunchukuttan, A., ... & Khapra, M. M. (2022). Aksharantar: Towards building open transliteration tools for the next billion users. arXiv preprint arXiv:2205.03018.

## Acknowledgements

Many thanks to discussions with Prafulla Chandra A and Sankeerth Rao K on bringing this to fruition