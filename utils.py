import torch
import torch.nn.functional as F
# Transliteration
from ai4bharat.transliteration import XlitEngine
# Embeddings
from transformers import BertModel, BertTokenizerFast
# Lyrics download
from lyrics.genius import get_lyrics as get_genius
from lyrics.openai import get_lyrics as get_openai


TRUNCATE_LENGTH = 512

# Embedding related
tokenizer = BertTokenizerFast.from_pretrained("setu4993/LaBSE")
model = BertModel.from_pretrained("setu4993/LaBSE")
model = model.eval()

# Transliteration related
engine = XlitEngine(["ta", "te"], beam_width=10, rescore=False)


def encode_text(text):
    encoded_input = tokenizer(
        text, return_tensors='pt', padding=True, truncation=True, max_length=TRUNCATE_LENGTH)
    with torch.no_grad():
        model_output = model(**encoded_input)
    return model_output.pooler_output


def cosine_similarity(a, b):
    normalized_a = F.normalize(a, p=2)
    normalized_b = F.normalize(b, p=2)
    return torch.matmul(
        normalized_a, normalized_b.transpose(0, 1)
    ).item()


def transliterate(text, code):
    return engine.translit_sentence(text, lang_code=code)


def similarity(a, b):
    # Convert to smallcase
    a = a.lower()
    b = b.lower()

    # Transliterate into respective languages
    t_a = transliterate(a, 'ta')
    t_b = transliterate(b, 'te')

    # Perform similarity matching
    print('Performing similarity between...')
    print(t_a[:25] + '...')
    print(t_b[:25] + '...')

    encoded_tamil = encode_text(t_a)
    encoded_telugu = encode_text(t_b)

    return cosine_similarity(encoded_tamil, encoded_telugu)


def get_lyrics_source(song_title, song_artist, source):
    if source == "genius":
        return get_genius(song_title, song_artist)
    elif source == "openai":
        return get_openai(song_title, song_artist)
    else:
        raise Exception('Incorrect method specified')
