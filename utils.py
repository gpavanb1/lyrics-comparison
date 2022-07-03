import spacy
from indic_transliteration import sanscript
from indic_transliteration.sanscript import transliterate
from translate import Translator

t_tamil = Translator(from_lang="ta", to_lang="en")
t_telugu = Translator(from_lang="te", to_lang="en")

nlp = spacy.load('en_core_web_md')

def similarity(a, b):
    # Convert to smallcase
    a = a.lower()
    b = b.lower()

    # Transliterate into respective languages
    t_a = transliterate(a, sanscript.HK, sanscript.TAMIL)
    t_b = transliterate(b, sanscript.HK, sanscript.TELUGU)

    # Translate output into English
    e_a = t_tamil.translate(t_a)
    e_b = t_telugu.translate(t_b)

    # Perform similarity matching
    print('Performing similarity between...')
    print(e_a[:25])
    print(e_b[:25])
    nlp_ea = nlp(e_a)
    nlp_eb = nlp(e_b)
    return nlp_ea.similarity(nlp_eb)
