"""
Get all companies names from a given text and also the count of them.
"""

import spacy

nlp = spacy.load('en_core_web_sm')

text = '''The Top 5 companies in USA are Tesla, Walmart, Amazon, Microsoft, Google and the top 5 companies in 
India are Infosys, Reliance, HDFC Bank, Hindustan Unilever and Bharti Airtel'''

companies = []
doc = nlp(text)
for ent in doc.ents:
    if ent.label_ == 'ORG':
        companies.append(ent.text)

print("Companies: ")
print(companies)
print("Count of Companies: ", len(companies))