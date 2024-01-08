"""
Extract all money transaction from below sentence along with currency. Output should be,
two $
500 €
"""

import spacy

transactions = "Tony gave two $ to Peter, Bruce gave 500 € to Steve"
nlp = spacy.blank("en")
doc = nlp(transactions)
for token in doc:
    if token.like_num and doc[token.i+1].is_currency:
        print(token, doc[token.i+1].text)