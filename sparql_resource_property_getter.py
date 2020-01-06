from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def get_resource(thing):
    thing = thing.replace(' ', '_')
    sparql.setQuery("""
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?type
        WHERE { <http://dbpedia.org/resource/""" + thing +"""> rdf:type ?type }
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    table = []
    for r in results['results']['bindings']:
        splitted = r['type']['value'].split('/')
        if splitted[2] == 'dbpedia.org' and splitted[3] == 'ontology':
            table.append({
                'label': splitted[-1],
                'url': r['type']['value']
            })
            
    return table


def get_property(word1, word2):
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT *
    WHERE { <http://dbpedia.org/resource/""" + word1 + """> ?label <http://dbpedia.org/resource/""" + word2 + """>}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    table = []
    for r in results['results']['bindings']:        
        splitted = r['label']['value'].split('/')
        if splitted[2] == 'dbpedia.org' and splitted[3] == 'property':
            table.append({
                'property': splitted[-1],
                'url': r['label']['value']
            })
    
    return table

def find_property(word1, word2, list_of_possible_types = []):
    word1, word2 = word1.replace(" ", "_"), word2.replace(" ", "_")
    
    table = [get_property(word1, word2), get_property(word2, word1)]
    table = [item for sublist in table for item in sublist]

    if len(list_of_possible_types) > 0:
        table = [item for item in table if item['property'] in list_of_possible_types]
   
    return table

if __name__ == "__main__":
    print("\n>> Resource of England")
    [print(x) for x in get_resource('England')]
    print("\n>> Resource of London")
    [print(x) for x in get_resource('London')]
    print("\n>> Property of England and London")
    [print(x) for x in find_property('England', 'London')]
    print("\n>> Property of England and London - possible capital")
    [print(x) for x in find_property('England', 'London', ['capital'])]