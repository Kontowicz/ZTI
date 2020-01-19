import sys

import nltk
from nltk.tokenize import word_tokenize

from nltk.tag import pos_tag, StanfordNERTagger

import spacy
from spacy import displacy
from collections import Counter
import en_core_web_sm


default_sentences = [
    'Barack Obama likes Google',
    'Richard Hendricks studied on Stanford University',
    'Lech Wałęsa was president of Poland',
    'Mona Lisa will meet you in the park',
    "Google CEO Sundar Pichai responded today to the firing of employee James"
    " Damore over his controversial memo on workplace diversity."
]


def process_using_pos_tag(sent):
    sent = nltk.word_tokenize(sent)
    tags = nltk.pos_tag(sent)
    return tags


def load_stanford_ner():
    base = 'stanford-ner-2018-10-16'
    class_path = f'{base}/classifiers/english.all.3class.distsim.crf.ser.gz'
    jar_path = f'{base}/stanford-ner.jar'
    staner = StanfordNERTagger(class_path, jar_path, encoding='utf-8')
    return staner


def process_using_stanford_ner(sent, staner):
    sent = nltk.word_tokenize(sent)
    classes = staner.tag(sent)
    return classes


def process_using_spacy(sent, en_core, format_result):
    entities = en_core(sent).ents
    if format_result:
        result = list(
            zip([e.text.lower() for e in entities], [e.label_ for e in entities]))
    else:
        result = entities
    return result


if __name__ == '__main__':
    data = []
    if len(sys.argv) > 1:
        sentences = sys.argv[1:]
    else:
        print('No sentences provided. Running for deafaul sentences')
        sentences = default_sentences

    print('Sentences:')
    for i, sent in enumerate(sentences):
        print(f'{i} : {sent}')

    print('\nResult 1 - NLTK pos_tag')
    for i, sent in enumerate(sentences):
        tags = process_using_pos_tag(sent)
        print(f'{i} : {tags}')

    print('\nResult 2 - NLTK Stanford NER')
    print('I G N O R E D')
    # staner = load_stanford_ner()
    # for i, sent in enumerate(sentences):
    #     tags = process_using_stanford_ner(sent, staner)
    #     print(f'{i} : {tags}')

    print('\nResult 3 - Spacy')
    en_core = en_core_web_sm.load()
    for i, sent in enumerate(sentences):
        objects = process_using_spacy(sent, en_core, format_result=True)
        print(f'{i} : {objects}')

    # print('\nResult 4 - Spacy with displacy')
    # en_core = en_core_web_sm.load()
    # for i, sent in enumerate(sentences):
    #     entities = process_using_spacy(sent, en_core, format_result=False)
    #     displacy.serve(entities, style='ent')
    #     displacy.serve(entities, style='dep', options={'distance': 120})
