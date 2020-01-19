import re

def parse_task_1_2(file, only_sentences=False):
    with open(file, 'r') as file:
        data = file.read().split('\n\n')
        is_string_re = 'nif:isString.*\"(.*)\"'
        anchorOf_re = 'nif:anchorOf.*\"(.*)\"'

        meta = {}
        sentences = {}

        for item in data:
            tmp = re.search(is_string_re, item)
            if tmp:
                sentences[tmp.group(1)] = item

            tmp = re.search(anchorOf_re, item)
            if tmp:
                meta[tmp.group(1)] = item

    if only_sentences:
        return list(sentences.keys())[0], sentences
    else:
        return meta, sentences


def parse_odp(file):
    with open(file, 'r') as file:
        data = file.read().split('\n\n')

        results = []
        for item in data:
            if item[:3] == '[ a' and item[-3:] == '] .':
                x3 = []
                for fi in item.split('\n')[1:4]:
                    x3.append(fi.split(':')[2][:-2].replace('_', '').lower())

                results.append(tuple(x3))


        return results