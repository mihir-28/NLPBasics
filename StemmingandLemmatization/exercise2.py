"""
Convert the given text into it's base form using both stemming and lemmatization
"""

import nltk
import spacy


from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

nlp = spacy.load("en_core_web_sm")

text = """Latha is very multi talented girl.She is good at many skills like dancing, running, singing, playing. She also likes eating Pav Bhagi. she has a habit of fishing and swimming too.Besides all this, she is a wonderful at cooking too.
"""

# Stemming in NLTK
tokens = nltk.word_tokenize(text)

base_tokens1 = []
for token in tokens:
    base_tokens1.append(stemmer.stem(token))

base_text1 = ' '.join(base_tokens1)
print("Stemming (NLTK): ")
print(base_text1)


# Lemmatization in SpaCy
doc = nlp(text)
base_tokens2 = []
for token in doc:
    base_tokens2.append(token.lemma_)

base_text2 = ' '.join(base_tokens2)
print("\nLemmatization (SpaCy): ")
print(base_text2)