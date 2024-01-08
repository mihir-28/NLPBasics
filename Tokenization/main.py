import spacy

nlp = spacy.blank('en')
doc = nlp("Tony gave two $ to Peter, Bruce gave 500 € to Steve")
print("Tokens in doc: ")
for token in doc:
    print(token)

print("\nToken attributes: ")
for token in doc:
    print(
        token, "==>",
        "index: ", token.i, 
        "is_alpha:", token.is_alpha, 
        "is_punct:", token.is_punct, 
        "like_num:", token.like_num, 
        "is_currency:", token.is_currency,
    )


#Collecting URLs & Emails
nlp = spacy.blank('en')
doc = nlp("Look for data to help you address the question. Governments are good sources because data from public research is often freely available. Good places to start include http://www.data.gov/, and http://www.science.gov/, and in the United Kingdom, http://data.gov.uk/. Two of my favorite data sets are the General Social Survey at http://www3.norc.org/gss+website/, and the European Social Survey at http://www.europeansocialsurvey.org/. Email at randomduck@git.com")

print("URLs in doc: ")
for token in doc:
    if token.like_url:
        print(token)
        
print("\nEmails in doc: ")
for token in doc:
    if token.like_email:
        print(token)


#Custom Tokenization
from spacy.symbols import ORTH
nlp = spacy.blank("en")
doc = nlp("gimme double cheese extra large healthy pizza")
nlp.tokenizer.add_special_case("gimme", [
    {ORTH: "gim"},
    {ORTH: "me"},
])
doc = nlp("gimme double cheese extra large healthy pizza")
tokens = [token.text for token in doc]
print(tokens)


#Sentence Segmentation
nlp = spacy.blank("en")
nlp.add_pipe('sentencizer')
doc = nlp("Dr. Strange loves pav bhaji of mumbai. Hulk loves chat of delhi")
for sentence in doc.sents:
    print(sentence)