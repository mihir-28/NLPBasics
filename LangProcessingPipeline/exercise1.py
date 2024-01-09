"""
Get all the proper nouns from a given text in a list and also count how many of them.
Proper Noun means a noun that names a particular person, place, or thing.
"""

import spacy

nlp = spacy.load('en_core_web_sm')

text = '''Sam and Raju are the best friends from school days.They wanted to go for a world tour and 
visit famous cities like Paris, London, Dubai, Rome etc and also they called their another friend Mohan to take part of this world tour.
They started their journey from Hyderabad and spent next 3 months travelling all the wonderful cities in the world and cherish a happy moments!
'''

propn = []
doc = nlp(text)
for token in doc:
    if token.pos == spacy.symbols.PROPN:
        propn.append(token.text)
print("Proper Nouns: ")
print(propn)
print("Count of Proper Nouns: ", len(propn))