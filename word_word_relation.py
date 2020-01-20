from dicts import *
import itertools
from nltk.stem import PorterStemmer 
from nltk.tokenize import word_tokenize 
from nltk.corpus import stopwords
import string
from sparql_resource_property_getter import new_getter


ps = PorterStemmer() 
stop_words = list(set(stopwords.words('english')) )


def get_relation(pary, sent):
    perm = list(itertools.permutations(pary, 2))
    
    sent = sent.translate(str.maketrans('', '', string.punctuation))
    sent = [ps.stem(w) for w in word_tokenize(sent) if not w in stop_words]
    
    rel = []
    for a,b in perm:
        if a[1] in ignore_list or b[1] in ignore_list:
                continue

        a_, b_ = new_getter(a[0]), new_getter(b[0])

        if len(a_) == 0:
            a_ = [maps.get(a[1], '')]

        if len(b_) == 0:
            b_ = [maps.get(b[1], '')]

        for a__ in a_:
            for b__ in b_:
                co = big_dict.get((a__, b__), '')

                for c in co:
                    if ps.stem(c) in sent:
                        rel.append((a, b, c))

                if len(rel) == 0:
                    for c in co:
                        rel.append((a, b, c))

    return rel