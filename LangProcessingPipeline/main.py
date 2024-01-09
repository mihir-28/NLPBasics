import spacy
nlp = spacy.load('en_core_web_sm')
doc = nlp("Adam and Eve loves pav bhaji of mumbai. John loves chat of delhi")
for ent in doc.ents:
    print(ent.text, ent.label_, spacy.explain(ent.label_))