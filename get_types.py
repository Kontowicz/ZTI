from SPARQLWrapper import SPARQLWrapper, JSON
sparql = SPARQLWrapper("http://dbpedia.org/sparql")

def find_types(word):
  table = []
  word = word.replace(" ", "_")
  sparql.setQuery("""
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    SELECT ?type
    WHERE { <http://dbpedia.org/resource/""" + word + """> rdf:type ?type }
    """)
  sparql.setReturnFormat(JSON)
  results = sparql.query().convert()

  for result in results['results']['bindings']:
      splitted = result['type']['value'].split('/')
      if splitted[2] == 'dbpedia.org' and splitted[3] == 'ontology':
        #print(splitted[-1])
        table.append(splitted[-1])
  return table