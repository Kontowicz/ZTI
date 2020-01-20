knowladge = [
    # coś, coś, relacja, słowa kluczowe do rozpoznania relacji
    ['ORG', 'ORG', 'affiliation', ['relate','affiliated']],
    ['Person', 'EducationalInstitution',  'almaMater', ['study','college','educated','graduated']],
    ['Band', 'Person', 'bandMember', ['play', 'music','band']],
    ['Person', 'Place', 'birth', ['birth', 'born','from']],
    ['Person', 'ORG', 'ceo', ['president', 'boss', 'head', 'chief','ceo']],
    ['Person', 'Person', 'child', ['child','son','daughter']],
    ['Athlete', 'SportsTeam', 'club', ['train', 'play','player','club','team']],
    ['ORG', 'country', 'country', ['located','from','in']],
    ['Person', 'country', 'country', ['located','from','in']],
    ['Place', 'country', 'country', ['located','from','in']],
    ['Person', 'Place',  'death', ['death','died','passed']],
    ['ATHLETE', 'SPOERTSTEAM', 'debutTeam', ['first','debut']],
    ['PopulatedPlace', 'PopulatedPlace', 'department', ['from', 'in','department']],
    ['Place', 'PopulatedPlace', 'district', ['in','district']],
    ['Scientist', 'Person', 'doctoralAdvisor', ['doctorate', 'doctoral']],
    ['Scientist', 'Person', 'doctoralStudent', ['doctorate', 'doctoral']],
    ['Person', 'ORG', 'employer', ['work', 'boss','employer']],
    ['Band', 'Person', 'formerBandMember', ['former']],
    ['Athlete', 'SportsTeam', 'formerTeam', ['played','former']],
    ['ORG', 'City', 'foundationPlace', ['in', 'located','from','founded']],
    ['ORG', 'PopulatedPlace', 'headquarter', ['in','located','headquarter']],
    ['ORG', 'Settlement', 'hometown', ['from','hometown','in']],
    ['Person', 'Settlement', 'hometown', ['from', 'lives','hometown']],  
    ['PopulatedPlace', 'Person', 'leaderName', ['president','congress','leader']],
    ['Place', 'Place', 'locatedInArea', ['from', 'in','at','located']],
    ['Person', 'Place', 'location', ['at','in','located']],
    ['ORG', 'Place', 'location', ['at','in','located']],
    ['Place', 'Place', 'location', ['at','in','located']],
    ['Person', 'Country', 'nationality', ['from','descent','nationality']],  
    ['Person', 'Person', 'parent', ['child','father','mother','guardian','parent']],
    ['ORG', 'Person', 'president', ['president','leader']],
    ['Person', 'ORG', 'president', ['president','leader']],
    ['Person', 'Person', 'relative', ['mother','son','daughter','relative','family']],
    ['Person', 'Person', 'spouse', ['wife', 'husband','spouse']], 
    ['Company', 'Company', 'subsidiary', ['subcontractor','contractor','subsidiary']],
    ['ArchitecturalStructure', 'ORG', 'tenant', ['rent','tenant','inhabit','inhabitany']],
    ['Athlete', 'Person', 'trainer', ['train','trainer']]
]

def get_synonims(word):
    from nltk.corpus import wordnet
    synonyms = []

    for syn in wordnet.synsets("active"):
        for l in syn.lemmas():
            synonyms.append(l.name())
    return synonyms

def add_synonims():
    import re
    for i in range(0, len(knowladge)):
        basic = knowladge[i][3]
        wide = []
        for item in basic:
            wide += get_synonims(item)
        wide += basic

        wide = list(set(wide))
        wide = [re.sub(r'[^a-zA-Z0-9 ]', ' ', word) for word in wide]
        
        knowladge[i][3] = list(set(wide))

def get_relations(zdanie, pary):        
    add_synonims()

    import copy
    zdanie = copy.copy(zdanie)
    zdanie = zdanie.lower()
    for item in pary:
        zdanie = zdanie.replace(item[0], item[0].replace(' ','_')+'|'+item[1])

    def in_first(word):
        to_return = []
        for item in knowladge:
            if word.lower() == item[0].lower():
                to_return.append(item)
        return to_return

    from nltk.stem import WordNetLemmatizer 
    
    lemmatizer = WordNetLemmatizer()
    import re
    zdanie = re.sub(r'[^a-zA-Z0-9 |]', '', zdanie)
    print(zdanie)
    zdanie = zdanie.split(' ')

    for i in range(0, len(zdanie)):
        tmp = []
        if '|' in zdanie[i]:
            tmp = in_first(zdanie[i].split('|')[1])

        if tmp != []:
            string = [lemmatizer.lemmatize(x.lower()) for x in zdanie[i+1::]]
            new_string = []
            for item in string:
                if '|' in item:
                    d = item.split('|')
                    new_string.append(d[0])
                    new_string.append(d[1])
                else:
                    new_string.append(item)

            for entry in tmp:
                if entry[1].lower() in new_string:
                    kw_find = new_string[0:new_string.index(entry[1].lower())]
                    for kw in entry[3]:
                        if lemmatizer.lemmatize(kw.lower()) in kw_find:
                            print('Relation: ' + zdanie[i].split('|')[0] + ' ' + entry[2] + ' ' + string[-1].split('|')[0])
                            p = zdanie[i].split('|')[0] + ' ' + entry[2] + ' ' + string[-1].split('|')[0]
                            return p.split(' ')

if '__main__' == __name__:
    from parse import parse_task_1_2
    sent, sentences = parse_task_1_2('training/file_39.ttl', only_sentences=True)
    from entities_recognition_tester import process_using_spacy
    import en_core_web_sm
    sent = 'Kim Jong-un became the supreme leader of North Korea in 2011, succeeding his father Kim Jong-il'
    pary = process_using_spacy(sent, en_core=en_core_web_sm.load(), format_result=True)

    get_relations(sent, pary)