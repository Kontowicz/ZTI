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
            table.append((r['type']['value'],splitted[-1]))
            
    return table


def get_property(word1, word2):
    sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?property
    WHERE { <http://dbpedia.org/resource/""" + word1 + """> ?property <http://dbpedia.org/resource/""" + word2 + """>}
    """)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()
    
    table = []
    for r in results['results']['bindings']:        
        splitted = r['property']['value'].split('/')
        if splitted[2] == 'dbpedia.org' and splitted[3] == 'property':
            table.append((r['property']['value'],splitted[-1]))
    
    return table

def find_property(word1, word2):
    word1, word2 = word1.replace(" ", "_"), word2.replace(" ", "_")
    
    table = [get_property(word1, word2), get_property(word2, word1)]
    table = [item for sublist in table for item in sublist]
   
    return table



print(get_resource('Poland'))
print(get_resource('Lech Wałęsa'))
print(find_property('England', 'London'))