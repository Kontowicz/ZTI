from parse import parse_task_1_2
from entities_recognition_tester import process_using_spacy
from word_word_relation import get_relation
import en_core_web_sm
import string

def clean_string(x):
    a,b,c = [x[1][0], x[2], x[0][0]]

    if b in a:
        a = ' '.join([aa for aa in a.split() if b not in aa or aa == 'the'])
    if b in c:
        c = ' '.join([aa for aa in c.split() if b not in aa or aa == 'the'])

    tab = a,b,c
    res_tab = []
    for aa in tab:
        aa = aa.replace(' ', '')
        aa = aa.translate(str.maketrans('', '', string.punctuation))
        aa = aa.strip()
        res_tab.append(aa)

    a, b, c = res_tab
    return (a, b, c)

def own_fun(file):
    sent, sentences = parse_task_1_2(file, only_sentences=True)
    pary = process_using_spacy(sent, en_core = en_core_web_sm.load(), format_result=True)
    rel = get_relation(pary, sent)

    res = [clean_string(x) for x in rel]

    return res

