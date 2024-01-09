import nltk
import spacy

from nltk.stem import PorterStemmer
from nltk.stem import WordNetLemmatizer

words = ["eating", "working", "eats", "eat", "ate", "adjustable", "rafting", "ability", "meeting"]

# Stemming in NLTK
stemmer = PorterStemmer()

print("Stemming (NLTK): ")
for word in words:
    print(word, "|", stemmer.stem(word))


# Lemmatization in NLTK
lemmatizer = WordNetLemmatizer()

print("\nLemmatization (NLTK): ")
for word in words:
    print(word, "|", lemmatizer.lemmatize(word))


# Lemmatization in SpaCy
nlp = spacy.load("en_core_web_sm")

text = "Mando talked for 3 hours although talking isn't his working thing"
doc = nlp(text)
print("\nLemmatization (SpaCy): ")
for token in doc:
    print(token.text, "|", token.lemma_)