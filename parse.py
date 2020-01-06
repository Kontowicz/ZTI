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