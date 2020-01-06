from dicts import *
import itertools
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import string

ps = PorterStemmer() 
stop_words = list(set(stopwords.words('english')) )


def get_relation(pary, sent):
    perm = list(itertools.permutations(pary, 2))
    
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    sent = [ps.stem(w) for w in word_tokenize(sent) if not w in stop_words]
    
    
    rel = []
    for a,b in perm:
        co = big_dict[(maps[a[1]], maps[b[1]])]
        for c in co:
            if ps.stem(c) in sent:
                rel.append((a, b, c))
    return rel