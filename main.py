import spacy

def pos_tagging(text):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(text)
    tagged = [(token.text, token.pos_) for token in doc]
    return tagged

# Example Usage
text = "I am learning Python programming."
tagged_text = pos_tagging(text)
print("Input: ", text)
print("Tagged Text:\n", tagged_text)