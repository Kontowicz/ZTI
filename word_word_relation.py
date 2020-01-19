from dicts import *
import itertools
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import string
from sparql_resource_property_getter import new_getter

ps = PorterStemmer() 
stop_words = list(set(stopwords.words('english')) )

def ask(el):
    a = sl.annotate('https://api.dbpedia-spotlight.org/en/annotate', el)[0]['types']
    a = [x for x in a.split(',') if 'DBpedia:' in x]

    if len(a)>0:
        a = a[0].split(':')[1]
    else:
        raise sl.SpotlightException
    return a


def get_relation(pary, sent):
    perm = list(itertools.permutations(pary, 2))
    
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    sent = [ps.stem(w) for w in word_tokenize(sent) if not w in stop_words]
    
    rel = []
    for a,b in perm:
        a_, b_ = new_getter(a[0]), new_getter(b[0])

        # print(a[0], a_, ' - ', b[0], b_)

        if len(a_) == 0:
            a_ = [maps.get(a[1], '')]

        if len(b_) == 0:
            b_ = [maps.get(b[1], '')]

        for a__ in a_:
            for b__ in b_:
                co = big_dict.get((a__, b__), '')
                if co == '':
                    co = big_dict.get((b__,a__), '')

                for c in co:
                    if ps.stem(c) in sent:
                        rel.append((a, b, c))

    return rel