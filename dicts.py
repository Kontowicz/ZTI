big_dict = {
     ('Organisation', 'Organisation'): ['affiliation'],
     ('Person', 'EducationalInstitution'): ['almaMater'],
     ('Band', 'Person'): ['formerBandMember', 'bandMember'],
     ('Person', 'Place'): ['deathPlace', 'birthPlace', 'location'],
     ('Organisation', 'Person'): ['president', 'ceo'],
     ('Person', 'Person'): ['spouse', 'relative', 'parent', 'child'],
     ('Athlete', 'SportsTeam'): ['formerTeam', 'debutTeam', 'club'],
     ('Organisation', 'Country'): ['country'],
     ('Person', 'Country'): ['country','nationality'],
     ('Place', 'Country'): ['country'],
     ('PopulatedPlace', 'PopulatedPlace'): ['department'],
     ('Place', 'PopulatedPlace'): ['district'],
     ('Scientist', 'Person'): ['doctoralStudent', 'doctoralAdvisor'],
     ('Person', 'Organisation'): ['employer'],
     ('Organisation', 'City'): ['foundationPlace'],
     ('Organisation', 'PopulatedPlace'): ['headquarter'],
     ('Organisation', 'Settlement'): ['hometown'],
     ('Person', 'Settlement'): ['hometown'],
     ('PopulatedPlace', 'Person'): ['leaderName'],
     ('Place', 'Place'): ['location','locatedInArea'],
     ('Organisation', 'Place'): ['location'],
     ('Company', 'Company'): ['subsidiary'],
     ('ArchitecturalStructure', 'Organisation'): ['tenant'],
     ('Athlete', 'Person'): ['trainer']
}

maps = {
    'ORG': 'Organisation',
    'PERSON': 'Person',
    'GPE': 'Place',
    'LOC': 'PopulatedPlace',
    'FAC': 'ArchitecturalStructure',
    'WORK_OF_ART': 'Band',
    'US' : 'UnitedStates'
}

ignore_list = [
    'DATE',
    'EVENT',
    'PERCENT',
    'NORP',
    'ORDINAL'
    'CARDINAL',
    'TIME'
]

delete_list = [
    (['Person'], ['Place', 'Location'])
]