"""You are parsing a news story from cnbc.com. News story is stored in file.txt which is available in this same folder on github.
You need to,
1. Extract all NOUN tokens from this story. You will have to read the file in python first to collect all the text and then extract NOUNs in a python list
2. Extract all numbers (NUM POS type) in a python list
3. Print a count of all POS tags in this story"""

import spacy

with open("file.txt", "r") as file:
    text = file.read()

num = []
noun = []

def pos_tagging(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    for token in doc:
        if token.pos_ == "NUM":
            num.append(token)
        elif token.pos_ == "NOUN":
            noun.append(token)

def pos_count(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    pos_counts = doc.count_by(spacy.attrs.POS)
    for k,v in sorted(pos_counts.items()):
        print(f"{k}. {doc.vocab[k].text:{6}}: {spacy.explain(doc.vocab[k].text)}: {v}")

tagged_text = pos_tagging(text)

print("Num_Tokens:\n", num)
print("\nNoun_Tokens:\n", noun)
print("\nPOS_Count:")
pos_count(text)