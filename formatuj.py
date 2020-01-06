def print_word(word, in_db, sent, meta):
    start_index = sent.find(word)
    end_index = start_index+len(word)

    word_ns = word.replace(' ', '_')

    print(meta.split('#')[0]+f'#char={start_index},{end_index}> ;')
    print('a  nif:RFC5147String , nif:String , nif:Phrase ;')
    print(f'nif:anchorOf  "{word}"^^xsd:string ;')
    print(f'nif:beginIndex  "{start_index}"^^xsd:nonNegativeInteger ;')
    print(f'nif:endIndex  "{end_index}"^^xsd:nonNegativeInteger ;')
    print('nif:referenceContext ' + meta + ' ;')

    if in_db:
        print(f'itsrdf:taIdentRef dbr:{word_ns} .')
    else:
        print(f'itsrdf:taIdentRef http://aksw.org/notInWiki/{word_ns} .')
        
    return word_ns

def print_relation(word_0, word_1, rel, meta):
    print('[]')
    print('a  rdf:Statement , oa:Annotation ;')
    print(f'rdf:object  dbr:{word_1} ;')
    print(f'rdf:predicate  dbo:{rel} ;')
    print(f'rdf:subject  aksw:{word_0} ;')
    print('oa:hasTarget [')
    print('a oa:SpecificResource;')
    print(f'oa:hasSource {meta} ] .')
    
def formatuj(rel, in_db, sent, meta):
    meta = meta.split('\n')[0]
    
    word_0 = print_word(rel[0][0], in_db[0], sent, meta)
    print()
    word_1 = print_word(rel[1][0], in_db[1], sent, meta)
    print()
    print_relation(word_0, word_1, rel[2], meta)