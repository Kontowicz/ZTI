from dicts import *
import itertools

def get_relation(pary, sent):
    perm = list(itertools.permutations(pary[1:], 2))
    
    rel = []
    for a,b in perm:
        co = big_dict[(maps[a[1]], maps[b[1]])]
        for c in co:
            if c in sent:
                rel.append((a, b, c))
    return rel