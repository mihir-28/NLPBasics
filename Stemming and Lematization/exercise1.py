"""
Convert these list of words into base form using Stemming and Lemmatization and observe the transformations.
"""

import nltk
import spacy

from nltk.stem import PorterStemmer
stemmer = PorterStemmer()
nlp = spacy.load("en_core_web_sm")

lst_words = ['running', 'painting', 'walking', 'dressing', 'likely', 'children', 'whom', 'good', 'ate', 'fishing']
print("Stemming (NLTK): ")
for word in lst_words:
    print(word, "|", stemmer.stem(word))

print("\nLemmatization (SpaCy): ")
for word in lst_words:
    doc = nlp(word)
    for token in doc:
        print(token.text, "|", token.lemma_)