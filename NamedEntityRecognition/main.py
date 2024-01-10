import spacy

nlp = spacy.load("en_core_web_sm")

text = """The Top 5 companies in USA are Tesla, Walmart, Amazon, Microsoft, Google and the top 5 companies in 
India are Infosys, Reliance, HDFC Bank, Hindustan Unilever and Bharti Airtel"""
doc = nlp(text)

for ent in doc.ents:
    print(ent.text, ent.label_)

print(nlp.pipe_labels['ner'])