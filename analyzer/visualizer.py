import spacy
from spacy import displacy

# 加载英文模型
nlp = spacy.load("en_core_web_sm")

def visualize_sentence(sentence):
    doc = nlp(sentence)
    displacy.serve(doc, style="dep")
