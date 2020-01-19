from parse import parse_task_1_2
from entities_recognition_tester import process_using_spacy
from word_word_relation import get_relation
import en_core_web_sm

def own_fun(file):
    sent, sentences = parse_task_1_2(file, only_sentences=True)
    pary = process_using_spacy(sent, en_core = en_core_web_sm.load(), format_result=True)
    rel = get_relation(pary, sent)

    res = [(x[1][0].replace(' ', ''),x[2].replace(' ', ''),x[0][0].replace(' ', '')) for x in rel]

    return res

