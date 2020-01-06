big_dict = {
     ('Organisation', 'Organisation'): ['affiliation'],
     ('Person', 'EducationalInstitution'): ['almaMater'],
     ('Band', 'Person'): ['formerBandMember', 'bandMember'],
     ('Person', 'Place'): ['deathPlace', 'birthPlace'],
     ('Organisation', 'Person'): ['president', 'ceo'],
     ('Person', 'Person'): ['spouse', 'relative', 'parent', 'child'],
     ('Athlete', 'SportsTeam'): ['formerTeam', 'debutTeam', 'club'],
     ('Organisation', 'Country'): ['country'],
     ('Person', 'Country'): ['country'],
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
     ('Place', 'Place'): ['locatedInArea'],
     ('Organisation', 'Place'): ['location'],
     ('Person', 'Place'): ['location'],
     ('Place', 'Place'): ['location'],
     ('Person', 'Country'): ['nationality'],
     ('Company', 'Company'): ['subsidiary'],
     ('ArchitecturalStructure', 'Organisation'): ['tenant'],
     ('Athlete', 'Person'): ['trainer']
}

maps = {
    'ORG': 'Organisation',
    'PERSON': 'Person',
    'GPE': 'Place'
}